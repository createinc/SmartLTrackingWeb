from __future__ import unicode_literals
import firebase_admin
from firebase_admin import auth
from firebase_admin import db
from firebase_admin import credentials
from django.conf import settings
from django.contrib import admin
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

cred = credentials.Certificate('/home/vishnu/Downloads/smartltracking-firebase-adminsdk-413gu-d5b91b1342.json')
default_app = firebase_admin.initialize_app(cred,{'databaseURL': "https://smartltracking.firebaseio.com"})
root = db.reference()
user_password = ""


'''Model for user datas'''

class UserProfile(models.Model):
    author = models.ForeignKey(User, null=True, editable=False, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100,blank=True,null=True,help_text=("enter the first name of user"))
    last_name = models.CharField(max_length=100,blank=True,null=True,help_text=("enter the last name"))
    address = models.CharField(max_length=300,blank=True,null=True,help_text=("enter the address"))
    contact = models.IntegerField(blank=True,null=True,help_text=("enter the contact"))
    email = models.EmailField(max_length=100,blank=True,null=True,help_text=("enter the email"))
    username = models.CharField(max_length=100,blank=True,null=True,help_text=("enter the username"))
    password = models.CharField(max_length=100,blank=True,null=True,help_text=("enter the strong password"))

    def __str__(self):
        return (self.username)


@receiver(post_save,sender=UserProfile)
def send_user_data_when_created_by_admin(sender, instance, **kwargs):
    first_name = instance.first_name
    last_name = instance.last_name
    address = instance.address
    contact = instance.contact
    email = instance.email
    username = instance.username
    user_password = instance.password
    message = "Unable to create account try again"
    html_content = "your first name:%s <br> last name:%s <br> " \
                     "address:%s <br> contact:%s <br> email:%s <br> username:%s <br> password:%s"
    from_email = settings.DEFAULT_FROM_EMAIL
    message=EmailMessage('welcome',html_content %
                           (first_name,last_name,address,contact,
                            email,username,user_password),from_email,[email])
    message.content_subtype='html'
    try:
        message.send()
    except:
        pass


class UserModel(admin.ModelAdmin):

    search_fields = ('first_name', 'email', 'username', )

    def save_model(self, request, obj, form, change):
        try:
            user = auth.create_user(
                email=obj.email,
                email_verified=False,
                password= obj.password,
                display_name=obj.username,
                disabled=False)
            datas = {
                'college_name': request.user.username,
                'status': 1
            }
            root.child('users').child(user.uid).set(datas)
        except Exception as e:
            messages.error(request, e)
            return
        if not change:
            obj.author = request.user
            obj.password = ''
        obj.save()

    def get_queryset(self, request):
        qs = super(UserModel, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(author=request.user)

    actions=['delete_selected_users']


    def get_actions(self, request):
        actions = super(UserModel, self).get_actions(request)
        del actions['delete_selected']
        return actions

    def delete_model(modeladmin, request, obj):
            user = auth.get_user_by_email(obj.email)
            auth.delete_user(user.uid)
            obj.delete()


    def delete_selected_users(self, request, queryset):
        for obj in queryset:
            try:
                user = auth.get_user_by_email(obj.email)
                auth.delete_user(user.uid)
            except:
                pass
            obj.delete()


'''Model for driver datas'''


class VehicleData(models.Model):
    author = models.ForeignKey(User, null=True, editable=False, on_delete=models.CASCADE,unique=False)
    username = models.CharField(max_length=100,blank=True,null=True,help_text=("enter the bus driver name"))
    bus_no = models.CharField(max_length=100,blank=True,null=True,help_text=("enter the bus number"))
    license_no = models.CharField(max_length=300,blank=True,null=True,help_text=("enter the license number"))
    contact = models.IntegerField(blank=True,null=True,help_text=("enter the contact"))
    bus_reg_no = models.CharField(max_length=100,blank=True,null=True,help_text=("enter the bus register number"))
    creation_date = models.DateTimeField(auto_now=True)
    last_modified = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (self.username)


class ModelVehicles(admin.ModelAdmin):

    search_fields = ('username', 'bus_reg_no', 'username', )

    def save_model(self, request, obj, form, change):
        try:
            datas = {
                'college_name': request.user.username,
                'driver_name': obj.username,
                'license_no': obj.license_no,
                'bus_no': obj.bus_no,
                'bus_reg_no': obj.bus_reg_no
                     }
            root.child(request.user.username).child('vehicles'). \
                child(obj.bus_no).set(datas)
        except:
            pass
        if not change:
            obj.author = request.user
        obj.save()



    def get_queryset(self, request):
        qs = super(ModelVehicles, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(author=request.user)

    actions=['delete_selected_users']


    def get_actions(self, request):
        actions = super(ModelVehicles, self).get_actions(request)
        del actions['delete_selected']
        return actions

    def delete_model(modeladmin, request, obj):
        root.child(request.user.username).child('vehicles'). \
            child(obj.bus_no).delete()
        obj.delete()

    def delete_selected_users(self, request, queryset):
        for obj in queryset:
            root.child(request.user.username).child('vehicles'). \
                child(obj.bus_no).delete()
            obj.delete()