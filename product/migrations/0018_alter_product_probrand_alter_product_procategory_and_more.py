# Generated by Django 4.1.1 on 2022-09-22 19:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0001_initial'),
        ('product', '0017_product_proisbestsaler_product_proisnew'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='PROBrand',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='settings.brand', verbose_name=' Brand'),
        ),
        migrations.AlterField(
            model_name='product',
            name='PROCategory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.category', verbose_name=' Category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='PRODiscription',
            field=models.TextField(max_length=1000, verbose_name=' Description'),
        ),
        migrations.AlterField(
            model_name='product',
            name='PROISBestsaler',
            field=models.BooleanField(default=False, verbose_name='Best Seller Product'),
        ),
        migrations.AlterField(
            model_name='product',
            name='PROISNew',
            field=models.BooleanField(default=True, verbose_name='New Product'),
        ),
        migrations.AlterField(
            model_name='product',
            name='PROSlug',
            field=models.SlugField(blank=True, null=True, verbose_name='Product URL'),
        ),
    ]
