# Generated by Django 2.1.2 on 2018-10-18 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evoting', '0003_auto_20181019_0236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voterslog',
            name='DoB',
            field=models.CharField(max_length=10),
        ),
    ]