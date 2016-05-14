# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import fluent_contents.extensions


class Migration(migrations.Migration):

    dependencies = [
        ('fluent_contents', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='JumbotronItem',
            fields=[
                ('contentitem_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='fluent_contents.ContentItem')),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('content', fluent_contents.extensions.PluginHtmlField(verbose_name='Content')),
                ('button_title', models.CharField(max_length=200, null=True, verbose_name='Button Title', blank=True)),
                ('button_url', fluent_contents.extensions.PluginUrlField(max_length=300, null=True, verbose_name='Button URL', blank=True)),
            ],
            options={
                'db_table': 'contentitem_fluentcms_jumbotron_jumbotronitem',
                'verbose_name': 'Jumbotron',
                'verbose_name_plural': 'Jumbotron',
            },
            bases=('fluent_contents.contentitem',),
        ),
    ]
