from django.contrib import admin
from . import models
import decimal

#admin.site.register(models.Product) # This will add Product to admin site
admin.site.register(models.Lig) # This will add Category to admin site
admin.site.register(models.Channel)
admin.site.register(models.Team)
admin.site.site_header = "Match live  Administration"

admin.site.site_title = "Match live Administration"

admin.site.index_title = ""


#def make_price_zero(modeladmin, request, queryset):
  # queryset.update(price=0)


#make_price_zero.short_description = "Make selected products free"


@admin.register(models.Match)
class MatchAdmin(admin.ModelAdmin):
    #date_hierarchy = 'create_at'
    search_fields = ['name']
    list_display = ('home_team_1', 'guest_team_2', 'stadium', 'commentator')
    #list_filter = ('Lig', 'create_at')
    #actions = [make_price_zero, discount]



# Register your models here.
