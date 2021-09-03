from currency.models import ContactUs, Rate, Source
from django.contrib import admin  # noqa


class RateAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'buy',
        'sale',
        'type',
        'source',
        'created',
    )
    list_filter = (
        'type',
        'source',
        'created',
    )
    search_fields = (
        'type',
        'source',
    )
    readonly_fields = (
        'buy',
        'sale',
    )

    def has_delete_permission(self, request, obj=None):
        return False


class ContactUsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'email_from',
        'subject',
        'message',
    )
    readonly_fields = (
        'email_from',
        'subject',
        'message',
    )

    def has_delete_permission(self, request, obj=None):
        return False


class SourceAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'source_url',
        'name',
    )


admin.site.register(Rate, RateAdmin)
admin.site.register(ContactUs, ContactUsAdmin)
admin.site.register(Source, SourceAdmin)
