# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import fluent_contents.extensions


class Migration(migrations.Migration):

    dependencies = [
        ('fluentcms_jumbotron', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jumbotronitem',
            old_name='button_title',
            new_name='button1_title',
        ),
        migrations.RenameField(
            model_name='jumbotronitem',
            old_name='button_url',
            new_name='button1_url',
        ),
        migrations.AddField(
            model_name='jumbotronitem',
            name='button2_title',
            field=models.CharField(max_length=200, null=True, verbose_name='Button 2 Title', blank=True),
        ),
        migrations.AddField(
            model_name='jumbotronitem',
            name='button2_url',
            field=fluent_contents.extensions.PluginUrlField(max_length=300, null=True, verbose_name='Button 2 URL', blank=True),
        ),
    ]
