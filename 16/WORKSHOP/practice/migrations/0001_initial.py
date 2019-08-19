# Generated by Django 2.2.4 on 2019-08-19 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=40)),
                ('birthday', models.DateField()),
                ('age', models.IntegerField()),
            ],
        ),
    ]
