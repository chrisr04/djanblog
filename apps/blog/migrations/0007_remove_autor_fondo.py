# Generated by Django 2.2.3 on 2019-07-31 01:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20190729_1549'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='autor',
            name='fondo',
        ),
    ]