# Generated by Django 2.2.1 on 2020-01-04 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(max_length=30)),
                ('plan_name', models.CharField(max_length=30)),
                ('price', models.IntegerField(default=0)),
                ('detail', models.TextField()),
            ],
        ),
    ]
