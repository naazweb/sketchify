# Generated by Django 3.1.1 on 2020-09-09 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('original_img', models.ImageField(null=True, upload_to='original/')),
                ('original_size', models.TextField(null=True)),
                ('converted_img', models.ImageField(null=True, upload_to='converted/')),
                ('converted_size', models.TextField(null=True)),
            ],
        ),
    ]
