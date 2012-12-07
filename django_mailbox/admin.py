from django.conf import settings
from django.contrib import admin

from django_mailbox.models import Message, Mailbox

def get_new_mail(mailbox_admin, request, queryset):
    for mailbox in queryset.all():
        mailbox.get_new_mail()
get_new_mail.short_description = 'Get new mail'

class MailboxAdmin(admin.ModelAdmin):
    list_display = (
                'name',
                'uri',
                'from_email',
                'active',
            )
    actions = [get_new_mail]

class MessageAdmin(admin.ModelAdmin):
    list_display = (
                'subject',
                'processed',
                'read',
                'mailbox',
                'outgoing',
            )
    ordering = ['-processed']
    list_filter = (
            'mailbox',
            'outgoing',
            'processed',
            'read',
            )
    raw_id_fields = (
            'in_reply_to',
            )

if getattr(settings, 'DJANGO_MAILBOX_ADMIN_ENABLED', True):
    admin.site.register(Message, MessageAdmin)
    admin.site.register(Mailbox, MailboxAdmin)
