from django.contrib import admin

from .models import Region

class RegionAdmin(admin.ModelAdmin):
	list_display =('nom_reg','id')


admin.site.register(Region,RegionAdmin)

from .models import Provincia

class ProvinciaAdmin(admin.ModelAdmin):
    list_display = ('id_prov','nom_prov')
    

admin.site.register(Provincia,ProvinciaAdmin)


from .models import Comuna

class ComunaAdmin(admin.ModelAdmin):
    list_display = ('id_com','nom_com')
    

admin.site.register(Comuna,ComunaAdmin)


from .models import Restaurant

class RestaurantAdmin(admin.ModelAdmin):
	list_display = ('id_rest','nombre','fono','web','clase','calle','numero')
	search_fields = ['nombre']
	list_filter = ['clase']
	#search_fields = ('nombre')
	
admin.site.register(Restaurant,RestaurantAdmin)




# Register your models here.
