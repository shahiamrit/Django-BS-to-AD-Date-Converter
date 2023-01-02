# Generated by Django 4.1.3 on 2023-01-02 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.ImageField(upload_to='cropped_images')),
                ('uploaded', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
