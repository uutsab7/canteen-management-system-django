# Generated by Django 3.0.5 on 2020-06-24 02:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('canteen_management_system', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cook',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]