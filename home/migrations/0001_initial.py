# Generated by Django 2.1.7 on 2019-02-23 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('show', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': '북마크 모음',
                'verbose_name': '북마크',
            },
        ),
    ]
