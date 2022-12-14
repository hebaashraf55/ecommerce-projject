# Generated by Django 4.1.1 on 2022-09-08 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PROName', models.CharField(max_length=50)),
                ('PRODiscription', models.TextField(max_length=1000)),
                ('PROImg', models.ImageField(upload_to='')),
                ('PROPrice', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='')),
                ('PROCoast', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='')),
                ('PROCreated', models.DateTimeField()),
            ],
        ),
    ]
