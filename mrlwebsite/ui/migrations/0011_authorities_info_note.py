# Generated by Django 3.0.5 on 2020-05-14 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ui', '0010_auto_20200514_2039'),
    ]

    operations = [
        migrations.AddField(
            model_name='authorities',
            name='info_note',
            field=models.TextField(blank=True, db_column='Remarks', null=True),
        ),
    ]
