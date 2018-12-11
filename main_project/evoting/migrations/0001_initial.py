# Generated by Django 2.1.3 on 2018-12-11 19:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='organiser_profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=50)),
                ('organiserId', models.CharField(max_length=10)),
                ('organiser', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Voters_Profile',
            fields=[
                ('fullname', models.CharField(blank=True, max_length=20)),
                ('voterId', models.CharField(blank=True, max_length=10, primary_key=True, serialize=False)),
                ('voter_dob', models.DateField()),
                ('region', models.CharField(choices=[('0', 'AndhraPradesh'), ('1', 'Bihar'), ('2', 'karnataka'), ('3', 'Tamilnadu'), ('4', 'Kerela'), ('5', 'UttarPradesh'), ('6', 'WestBengal'), ('7', 'MadhyaPradesh'), ('8', 'Haryana'), ('9', 'Assam')], max_length=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
