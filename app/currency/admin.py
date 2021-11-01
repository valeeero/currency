from accounts.models import User

from currency.models import ContactUs, Rate, ResponseLog, Source
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


class ResponseLogAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'created',
        'status_code',
        'path',
        'response_time',
        'request_method',
    )


class UserAdmin(admin.ModelAdmin):
    list_display = (
        'USERNAME_FIELD',
        'REQUIRED_FIELDS',
        'phone',
        'email',
        'id',
    )


admin.site.register(Rate, RateAdmin)
admin.site.register(ContactUs, ContactUsAdmin)
admin.site.register(Source, SourceAdmin)
admin.site.register(ResponseLog, ResponseLogAdmin)
admin.site.register(User, UserAdmin)
