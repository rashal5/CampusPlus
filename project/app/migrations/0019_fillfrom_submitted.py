# Generated by Django 4.2.7 on 2024-01-11 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_remove_userclick_user_delete_useraction_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='fillfrom',
            name='submitted',
            field=models.BooleanField(default=False),
        ),
    ]