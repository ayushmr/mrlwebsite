# Generated by Django 3.0.5 on 2020-05-15 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ui', '0017_auto_20200515_1009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commodities',
            name='com_type',
            field=models.CharField(choices=[('RAW AGRICULTURAL', 'RAW AGRICULTURAL'), ('PROCESSED', 'PROCESSED')], db_column='com-type', max_length=16, null=True),
        ),
    ]
