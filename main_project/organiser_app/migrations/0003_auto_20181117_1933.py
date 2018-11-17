# Generated by Django 2.1.2 on 2018-11-17 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organiser_app', '0002_candidate_candidate_election_election_region_vote_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='candidate_party',
            field=models.CharField(choices=[('BJP', 'Bhartiya Janta Party'), ('AAP', 'Aam Aadmi Party'), ('TDP', 'Telugu Desam Party'), ('TRS', 'Telangana Rashtra Samithi'), ('SP', 'Samajwadi Party'), ('JD', 'Janata Dal'), ('RJD', 'Rashtriya Janata Dal'), ('CPI', 'Communist Party of India'), ('INC', 'Indian National Congress'), ('SS', 'Shiv Sena')], max_length=10),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='candidate_region',
            field=models.CharField(choices=[('0', 'AndhraPradesh'), ('1', 'Bihar'), ('2', 'karnataka'), ('3', 'Tamilnadu'), ('4', 'Kerela'), ('5', 'UttarPradesh'), ('6', 'WestBengal'), ('7', 'MadhyaPradesh'), ('8', 'Haryana'), ('9', 'Assam')], max_length=10),
        ),
        migrations.AlterField(
            model_name='election_region',
            name='region',
            field=models.CharField(choices=[('0', 'AndhraPradesh'), ('1', 'Bihar'), ('2', 'karnataka'), ('3', 'Tamilnadu'), ('4', 'Kerela'), ('5', 'UttarPradesh'), ('6', 'WestBengal'), ('7', 'MadhyaPradesh'), ('8', 'Haryana'), ('9', 'Assam')], max_length=10),
        ),
        migrations.AlterField(
            model_name='voter',
            name='voter_gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Others')], max_length=10),
        ),
        migrations.AlterField(
            model_name='voter',
            name='voter_region',
            field=models.CharField(choices=[('0', 'AndhraPradesh'), ('1', 'Bihar'), ('2', 'karnataka'), ('3', 'Tamilnadu'), ('4', 'Kerela'), ('5', 'UttarPradesh'), ('6', 'WestBengal'), ('7', 'MadhyaPradesh'), ('8', 'Haryana'), ('9', 'Assam')], max_length=10),
        ),
    ]
