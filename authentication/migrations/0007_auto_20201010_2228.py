# Generated by Django 3.1.1 on 2020-10-10 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0006_auto_20201010_2226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(default='avtar_default.jpg', null=True, upload_to='user_avatar'),
        ),
    ]
