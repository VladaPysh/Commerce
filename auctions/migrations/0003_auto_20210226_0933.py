# Generated by Django 3.1.4 on 2021-02-26 09:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_auto_20210225_1034'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='status',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='listing',
            name='bid',
            field=models.ManyToManyField(default=None, to='auctions.Bid'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='category',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='auctions.category'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='comment',
            field=models.ManyToManyField(default=None, to='auctions.Comment'),
        ),
    ]
