# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-02-16 07:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_mailbox', '0006_mailbox_last_polling'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='eml',
            field=models.FileField(blank=True, help_text='Original full content of message', null=True, upload_to=b'messages', verbose_name='Raw message contents'),
        ),
    ]
