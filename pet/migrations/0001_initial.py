# Generated by Django 4.1.7 on 2023-03-30 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('age', models.PositiveIntegerField(default=0)),
                ('size', models.IntegerField(choices=[(0, 'Mini'), (1, 'Sm'), (2, 'Sm Md'), (3, 'Md'), (4, 'Md Bg'), (5, 'Bg'), (6, 'Xl')], default=0)),
                ('first_trait', models.IntegerField(choices=[(0, 'Active'), (1, 'Calm'), (2, 'Polite'), (3, 'Playful'), (4, 'Tender'), (5, 'Kind')], default=0)),
                ('second_trait', models.IntegerField(choices=[(0, 'Active'), (1, 'Calm'), (2, 'Polite'), (3, 'Playful'), (4, 'Tender'), (5, 'Kind')], default=0)),
            ],
        ),
    ]
