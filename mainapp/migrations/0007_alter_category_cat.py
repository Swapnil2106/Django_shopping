# Generated by Django 3.2.2 on 2021-07-14 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0006_alter_ordermodel_orderitems'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='cat',
            field=models.CharField(default=None, max_length=20),
        ),
    ]
