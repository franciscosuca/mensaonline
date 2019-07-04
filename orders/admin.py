from django.contrib import admin

from . models import Order

class OrderAdmin(admin.ModelAdmin):
    #date_hierarchy = 'timestamp'
    #search_fields = ['customer', 'menu']
    list_display = ['status', 'timestamp', 'update']
    #list_editable = ['status']
    #list_filter = ['price_student', 'status', 'category']
    readonly_fields = ['update', 'timestamp']
    class Meta:
        model = Order

admin.site.register(Order, OrderAdmin)

#admin.site.register(Order)
