import admin_thumbnails
from django.contrib import admin
from .models import Unit, Amenity, Country, City, Area, Images


@admin_thumbnails.thumbnail('image')
class UnitImageInline(admin.TabularInline):
    model = Images
    readonly_fields = ('id',)
    extra = 1

@admin_thumbnails.thumbnail('image')
class ImagesAdmin(admin.ModelAdmin):
    list_display = ['image','title','image_thumbnail']


@admin_thumbnails.thumbnail('image')
class UnitAdmin(admin.ModelAdmin):
    list_display = ['title', 'num_bedrooms', 'type','active', 'country','country', 'area', 'image_thumbnail']
    list_filter = ['type']
    search_fields = ['title', 'num_bedrooms', 'type']
    #readonly_fields = ('image_tag',)
    inlines = [UnitImageInline]
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Unit, UnitAdmin)
admin.site.register(Amenity)
admin.site.register(Country)
admin.site.register(City)
admin.site.register(Area)
admin.site.register(Images,ImagesAdmin)
