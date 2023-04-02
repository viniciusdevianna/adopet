# Generated by Django 4.1.7 on 2023-04-02 23:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0002_alter_profile_is_tutor_alter_profile_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='is_tutor',
            field=models.IntegerField(choices=[(0, 'Não'), (1, 'Sim')], default=0),
        ),
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('species', models.CharField(choices=[('D', 'Cão'), ('C', 'Gato'), ('B', 'Pássaro'), ('O', 'Outra')], default='D', max_length=1)),
                ('age', models.PositiveIntegerField(default=0)),
                ('size', models.CharField(choices=[('MIN', 'Mini'), ('SMA', 'Pequeno'), ('SMD', 'Pequeno/Médio'), ('MED', 'Médio'), ('MDB', 'Médio/Grande'), ('BIG', 'Grande'), ('VBG', 'Enorme')], default='MIN', max_length=3)),
                ('first_trait', models.CharField(blank=True, choices=[('ACT', 'Ativo'), ('CAL', 'Calmo'), ('POL', 'Educado'), ('PLA', 'Brincalhão'), ('TEN', 'Carinhoso'), ('KIN', 'Gentil')], default='ACT', max_length=3)),
                ('second_trait', models.CharField(blank=True, choices=[('ACT', 'Ativo'), ('CAL', 'Calmo'), ('POL', 'Educado'), ('PLA', 'Brincalhão'), ('TEN', 'Carinhoso'), ('KIN', 'Gentil')], default='ACT', max_length=3)),
                ('tutor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
