# Generated by Django 5.0.2 on 2024-02-08 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(upload_to='image/')),
                ('role', models.CharField(max_length=500)),
                ('role_description', models.TextField(max_length=500)),
            ],
        ),
    ]
