# Generated by Django 3.1.5 on 2021-04-03 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companion_app', '0002_auto_20210403_2304'),
    ]

    operations = [
        migrations.CreateModel(
            name='Disease',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disease_name', models.CharField(max_length=255)),
                ('speciality', models.CharField(max_length=255)),
            ],
        ),
    ]
