# Generated by Django 3.2.12 on 2024-01-10 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cards',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('front', models.CharField(max_length=100, verbose_name='FrontCard')),
                ('back', models.CharField(max_length=100, verbose_name='BackCard')),
            ],
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
    ]
