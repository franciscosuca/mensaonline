from django.contrib import admin

from . models import Invoice

class InvoiceAdmin(admin.ModelAdmin):
    #date_hierarchy = 'timestamp'
    #search_fields = ['customer', 'menu']
    list_display = ['status', 'timestamp', 'update']
    #list_editable = ['status']
    #list_filter = ['price_student', 'status', 'category']
    readonly_fields = ['update', 'timestamp']
    class Meta:
        model = Invoice

admin.site.register(Invoice, InvoiceAdmin)


