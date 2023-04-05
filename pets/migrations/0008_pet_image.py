# Generated by Django 4.1.7 on 2023-04-05 20:35

from django.db import migrations, models
import pets.models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0007_alter_profile_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='image',
            field=models.ImageField(default='media/not_found.jpg', upload_to=pets.models.pet_img_directory_path),
        ),
    ]
