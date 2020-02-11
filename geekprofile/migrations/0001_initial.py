# Generated by Django 3.0.3 on 2020-02-11 02:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street_addr', models.CharField(max_length=100)),
                ('apt_suite_unit', models.CharField(blank=True, max_length=25)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=25)),
                ('zipcode', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='CreditCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('number', models.CharField(max_length=16)),
                ('expire', models.CharField(max_length=7)),
                ('code', models.CharField(max_length=4)),
                ('zipcode', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('nickname', models.CharField(max_length=25)),
                ('creditcard', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='geekprofile.CreditCard')),
                ('home_address', models.ManyToManyField(to='geekprofile.Address')),
            ],
        ),
    ]
