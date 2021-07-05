# Generated by Django 3.2.4 on 2021-07-05 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocka_api', '0004_auto_20210705_0503'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchase',
            name='barcode',
        ),
        migrations.RemoveField(
            model_name='sale',
            name='barcode',
        ),
        migrations.AddField(
            model_name='product',
            name='barcode',
            field=models.CharField(blank=True, max_length=255, null=True, unique=True),
        ),
        migrations.DeleteModel(
            name='ProductBarcode',
        ),
    ]