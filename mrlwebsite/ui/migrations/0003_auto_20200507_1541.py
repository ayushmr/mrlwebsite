# Generated by Django 3.0.5 on 2020-05-07 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ui', '0002_auto_20200507_0054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='master',
            name='status_of_expire_date',
            field=models.CharField(blank=True, choices=[('Proposed', 'Proposed'), ('Fixed', 'Fixed')], db_column='Status_of_expire_date', default=None, max_length=8, null=True),
        ),
    ]