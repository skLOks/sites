# Generated by Django 4.2.5 on 2023-10-02 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='back',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cover', models.ImageField(upload_to='images/')),
                ('name', models.CharField(max_length=200, verbose_name='Имя устройства')),
                ('info', models.TextField(verbose_name='Информация')),
                ('price', models.CharField(max_length=200, verbose_name='Цена')),
            ],
        ),
    ]
