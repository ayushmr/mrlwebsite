# Generated by Django 3.0.5 on 2020-05-14 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ui', '0009_auto_20200514_2017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='master',
            name='Limit_type',
            field=models.CharField(choices=[('Default', 'Default'), ('General', 'General'), ('Organic MRLs', 'Organic MRLs')], db_column='MRL_type', default='Default', max_length=20),
        ),
    ]
