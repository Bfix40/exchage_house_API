# Generated by Django 3.2 on 2022-08-30 18:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_currency_trackfee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trackfee',
            name='base_currency',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='base', to='core.currency'),
        ),
        migrations.AlterField(
            model_name='trackfee',
            name='quote_currency',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='quote', to='core.currency'),
        ),
    ]
