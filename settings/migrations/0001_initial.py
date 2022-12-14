# Generated by Django 4.1.1 on 2022-09-10 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BRAName', models.CharField(max_length=40, verbose_name='Brand Name')),
                ('BRADesc', models.TextField(blank=True, max_length=400, null=True)),
            ],
            options={
                'verbose_name': 'Brand',
                'verbose_name_plural': 'Brands',
            },
        ),
        migrations.CreateModel(
            name='Variant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('VARName', models.CharField(max_length=40, verbose_name='Variant Name')),
                ('VARDesc', models.TextField(blank=True, max_length=400, null=True)),
            ],
            options={
                'verbose_name': 'Variant',
                'verbose_name_plural': 'Variants',
            },
        ),
    ]
