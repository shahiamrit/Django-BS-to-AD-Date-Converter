# Generated by Django 4.0.5 on 2023-01-04 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NEC', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userlogin',
            name='scode',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
