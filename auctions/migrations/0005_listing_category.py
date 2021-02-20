# Generated by Django 3.1.4 on 2021-02-20 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_auto_20210219_1357'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='category',
            field=models.CharField(choices=[('f', 'food'), ('e', 'electronics'), ('c', 'clothes')], default='category', max_length=1),
        ),
    ]
