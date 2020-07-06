# Generated by Django 3.0.4 on 2020-04-03 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='professor',
            fields=[
                ('name', models.TextField()),
                ('professor_id', models.AutoField(primary_key=True, serialize=False)),
                ('password', models.TextField(max_length=254)),
                ('email', models.EmailField(max_length=254)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
