# Generated by Django 4.2.1 on 2023-05-19 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='orgaisation_website',
            field=models.CharField(default=None, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='organisation_address',
            field=models.CharField(default=None, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='organisation_contact',
            field=models.CharField(default=None, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='organization_name',
            field=models.CharField(default=None, max_length=100, null=True),
        ),
    ]
