# Generated by Django 3.1.5 on 2021-04-04 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companion_app', '0003_disease'),
    ]

    operations = [
        migrations.AddField(
            model_name='disease',
            name='description',
            field=models.TextField(default='No infromation', max_length=9000),
        ),
    ]
