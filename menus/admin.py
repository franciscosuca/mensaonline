from django.contrib import admin

# Register your models here.

from . models import Menu

class MenuAdmin(admin.ModelAdmin):
    #date_hierarchy = 'timestamp'
    search_fields = ['title', 'status']
    list_display = ['title', 'category', 'status', 'price_student', 'price_guest', 'price_attendant', 'day']
    #list_editable = ['status']
    #list_filter = ['price_student', 'status', 'category']
    readonly_fields = ['update', 'timestamp']
    prepopulated_fields = {"slug": ("title",)}
    class Meta:
        model = Menu

admin.site.register(Menu, MenuAdmin)