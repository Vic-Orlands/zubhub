# Generated by Django 2.2.7 on 2021-04-02 03:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0030_auto_20210402_0216'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'categories'},
        ),
    ]