# Generated by Django 2.2.12 on 2020-05-07 21:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0022_copy_image_field_data_to_card_image_field'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='image',
        ),
    ]