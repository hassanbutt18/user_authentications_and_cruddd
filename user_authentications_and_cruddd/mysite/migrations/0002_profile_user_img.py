# Generated by Django 4.0.4 on 2022-04-18 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='user_Img',
            field=models.ImageField(default='default.jpg', upload_to='images/'),
        ),
    ]
