# Generated by Django 3.0.4 on 2021-06-03 11:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('admin_panel', '0002_exercise'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserFood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_food', to='admin_panel.Food')),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_food', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserExercises',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ex', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_ex', to='admin_panel.Exercise')),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_exercises', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]