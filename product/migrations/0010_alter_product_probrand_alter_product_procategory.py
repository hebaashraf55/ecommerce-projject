# Generated by Django 4.1.1 on 2022-09-10 21:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0001_initial'),
        ('product', '0009_product_probrand_product_procategory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='PROBrand',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='settings.brand', verbose_name='Product Brand'),
        ),
        migrations.AlterField(
            model_name='product',
            name='PROCategory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.category', verbose_name='Product Category'),
        ),
    ]
