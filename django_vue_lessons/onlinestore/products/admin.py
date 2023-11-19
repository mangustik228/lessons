from django.contrib import admin

# Register your models here.

import products.models as M


class ReceptionDescAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at", "updated_at")


admin.site.register(M.Product)
admin.site.register(M.Manufacturer)
admin.site.register(M.Color)
admin.site.register(M.ReceptionDesc, ReceptionDescAdmin)
