from django.contrib import admin
from .models import Advertisement
from .apps import AppAdvConfig
# Register your models here.

class Adv_admin(admin.ModelAdmin):
    list_display = ["id","auction", "title", "description", "price", "cteated_date", "updated_date"]
    list_display_links = [ "title"]
    list_filter = ["updated_at", "title"]
    list_per_page = 50
    actions = ["make_auctions_as_false", "make_auctions_as_true" ] # need function to work 
    fieldsets = (
        ('Main', {
            "fields":("title", "description")}),
        ('Finance', {
            "fields":("price", "auction"),
            #"collapse":["collapse"] # doesn't work Fieldset.__init__() got an unexpected keyword argument 'collapse'
        }))
    # function name same as in action
    @admin.action(description="Disable auction option")
    def make_auctions_as_false(self, request, queryset):
        queryset.update(auction=False)
    
    @admin.action(description="Enable auction option")
    def make_auctions_as_true(self, request, queryset):
        queryset.update(auction=True)
    

    
admin.site.register(Advertisement, Adv_admin)
