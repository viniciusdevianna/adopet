# Generated by Django 4.1.7 on 2023-04-05 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0006_remove_adoption_shelter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.CharField(blank=True, max_length=15),
        ),
    ]