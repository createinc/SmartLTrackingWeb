from django.contrib import admin
from users.models import UserProfile,UserModel
from users.models import ModelVehicles,VehicleData

admin.site.register(UserProfile,UserModel)
admin.site.register(VehicleData,ModelVehicles)
# Register your models here.
