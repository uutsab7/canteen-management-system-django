# Generated by Django 3.0.5 on 2020-06-24 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin_identity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('teacher_id', models.IntegerField()),
                ('address', models.CharField(max_length=10)),
            ],
        ),
    ]
