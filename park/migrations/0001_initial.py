# Generated by Django 5.2.4 on 2025-07-20 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Park',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название')),
                ('city', models.CharField(max_length=100, verbose_name='Город')),
                ('address', models.TextField(verbose_name='Адрес')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('is_work', models.BooleanField(default=True, verbose_name='Работает')),
                ('schedule', models.CharField(max_length=200, verbose_name='Расписание работы')),
            ],
        ),
    ]
