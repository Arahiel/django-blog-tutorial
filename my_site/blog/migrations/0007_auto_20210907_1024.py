# Generated by Django 3.2.6 on 2021-09-07 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20210830_1444'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image_name',
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='coding.jpg', upload_to='images'),
            preserve_default=False,
        ),
    ]
