# Generated by Django 3.2.5 on 2021-07-07 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_product_p_specification'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='p_sub_cat',
            field=models.CharField(choices=[('fashion', (('kids', 'kids'), ('womens', 'womens'), ('mens', 'mens'))), ('electronics', (('mobile', 'mobile'), ('laptop', 'laptop'), ('ipad', 'ipad'), ('power bank', 'power bank'))), ('accessories', (('earring', 'earring'), ('earphone', 'earphone'), ('watch', 'watch'), ('sunglass', 'sunglass')))], default='pant', max_length=100),
        ),
    ]
