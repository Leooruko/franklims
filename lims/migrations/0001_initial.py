# Generated by Django 5.0 on 2024-01-01 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sample',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registered', models.DateTimeField(auto_now_add=True)),
                ('sampleId', models.CharField(max_length=150)),
                ('sampleName', models.CharField(max_length=150)),
                ('industry', models.CharField(max_length=150)),
                ('client', models.CharField(max_length=150)),
                ('phoneNumber', models.CharField(max_length=150)),
                ('stage', models.CharField(max_length=150)),
                ('analysis', models.CharField(max_length=5000)),
                ('recommended', models.DateTimeField()),
                ('recommendation', models.CharField(max_length=5000)),
                ('invoiced', models.DateTimeField()),
            ],
        ),
    ]