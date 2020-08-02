from django.contrib import admin
from django.utils.html import format_html
from .models import vehicles,max_values

# Register your models here.
class vehicleadmin(admin.ModelAdmin):
    model='vehicles'
    list_display=['vehicle_name','mileage','price','image']
    
    def image(self,obj):
        return format_html(u'<img src="%s" style="width:100px;height:100px" />' % obj.vehicle_image.url.replace("vehicleapp/","/"))
    
admin.site.register(vehicles,vehicleadmin)





class max_valuesadmin(admin.ModelAdmin):
    model='max_values'
    list_display=['mileage','price']

admin.site.register(max_values,max_valuesadmin)