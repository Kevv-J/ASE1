# Generated by Django 2.1.2 on 2018-11-24 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evoting', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voters_profile',
            name='voterId',
            field=models.CharField(blank=True, max_length=10, primary_key=True, serialize=False),
        ),
    ]