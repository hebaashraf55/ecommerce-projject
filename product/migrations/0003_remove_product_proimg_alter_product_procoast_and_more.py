# Generated by Django 4.1.1 on 2022-09-09 15:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_alter_product_procoast_alter_product_proprice'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='PROImg',
        ),
        migrations.AlterField(
            model_name='product',
            name='PROCoast',
            field=models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Cost'),
        ),
        migrations.AlterField(
            model_name='product',
            name='PROCreated',
            field=models.DateTimeField(verbose_name='Created At '),
        ),
        migrations.AlterField(
            model_name='product',
            name='PRODiscription',
            field=models.TextField(max_length=1000, verbose_name='Product Description'),
        ),
        migrations.AlterField(
            model_name='product',
            name='PROName',
            field=models.CharField(max_length=50, verbose_name='Product Name'),
        ),
        migrations.AlterField(
            model_name='product',
            name='PROPrice',
            field=models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Price'),
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PROImage', models.ImageField(upload_to='product/', verbose_name='Image')),
                ('PROIproduct', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product', verbose_name='Product')),
            ],
        ),
    ]
