# Generated by Django 2.2.6 on 2019-11-01 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Auto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(default='', max_length=200)),
                ('anio', models.IntegerField()),
                ('color', models.CharField(default='', max_length=200)),
                ('stock', models.BooleanField(default=False)),
                ('marca', models.CharField(default='', max_length=200)),
            ],
        ),
    ]
