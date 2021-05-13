# Generated by Django 3.0.4 on 2021-05-05 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('img', models.ImageField(upload_to='food/images/')),
                ('calories', models.TextField()),
                ('proteins', models.TextField()),
                ('fats', models.TextField()),
                ('carbo', models.TextField()),
            ],
        ),
    ]
