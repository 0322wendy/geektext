# Generated by Django 3.0.3 on 2020-03-01 16:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('geekprofile', '0003_auto_20200211_1025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='creditcard',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='geekprofile.CreditCard'),
        ),
    ]
