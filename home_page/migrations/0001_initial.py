# Generated by Django 3.2.4 on 2021-10-03 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserReg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user1', models.CharField(max_length=60)),
                ('donardts', models.CharField(max_length=50)),
                ('bdgroup', models.CharField(max_length=40)),
                ('age', models.CharField(max_length=40)),
            ],
        ),
    ]
