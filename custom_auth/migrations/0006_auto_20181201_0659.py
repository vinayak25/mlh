# Generated by Django 2.1.1 on 2018-12-01 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_auth', '0005_permissionrole_permission'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='permissionrole',
            name='permission',
        ),
        migrations.RemoveField(
            model_name='permissionrole',
            name='role',
        ),
        migrations.AddField(
            model_name='role',
            name='permission',
            field=models.ManyToManyField(to='custom_auth.Permission'),
        ),
        migrations.DeleteModel(
            name='PermissionRole',
        ),
    ]
