# Generated by Django 2.1.1 on 2018-12-01 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_auth', '0002_auto_20181201_0621'),
    ]

    operations = [
        migrations.CreateModel(
            name='PermissionRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.ManyToManyField(to='custom_auth.Role')),
            ],
        ),
    ]
