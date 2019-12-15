from django.contrib import admin

from .forms import ServiceProviderAdminForm
from .models import ServiceProvider


@admin.register(ServiceProvider)
class ServiceProviderAdmin(admin.ModelAdmin):
    list_filter = ['active', '_sign_response', '_sign_assertion', '_signing_algorithm', '_digest_algorithm', '_encrypt_saml_responses']
    list_display = ['__str__', 'active', 'description']
    readonly_fields = ('dt_created', 'dt_updated', 'resulting_config')
    form = ServiceProviderAdminForm

    fieldsets = (
        ('Identification', {
            'fields': ('entity_id', 'pretty_name', 'description', 'metadata')
        }),
        ('Configuration', {
            'fields': ('active', '_processor', '_attribute_mapping', '_nameid_field', '_sign_response', '_sign_assertion', '_signing_algorithm', '_digest_algorithm', '_encrypt_saml_responses'),
        }),
        ('Resulting config', {
            'fields': ('dt_created', 'dt_updated', 'resulting_config')
        })
    )
