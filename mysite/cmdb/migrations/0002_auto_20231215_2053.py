# Generated by Django 3.2 on 2023-12-15 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('num', models.CharField(default=None, max_length=12)),
                ('name', models.CharField(default=None, max_length=1000)),
                ('score', models.IntegerField(default=1)),
                ('price', models.CharField(default=None, max_length=10)),
                ('ISBN', models.CharField(default=None, max_length=15)),
                ('author', models.CharField(default=None, max_length=1000)),
                ('publisher', models.CharField(default=None, max_length=50)),
                ('img', models.ImageField(default=None, upload_to='')),
                ('website', models.CharField(default=None, max_length=120)),
                ('sales', models.IntegerField(default=0, max_length=10)),
            ],
        ),
        migrations.RemoveField(
            model_name='mycollect',
            name='score',
        ),
    ]