# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_picture', '0007_fix_alignment'),
    ]

    operations = [
        migrations.AddField(
            model_name='picture',
            name='picture_rounded',
            field= models.BooleanField(default=False, help_text='Adds the .rounded class for round corners.', verbose_name='Rounded'),
        ),
    ]
