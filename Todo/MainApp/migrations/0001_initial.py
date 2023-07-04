# Generated by Django 4.1.7 on 2023-07-04 15:23

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TodoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateCreated', models.DateTimeField(auto_now_add=True)),
                ('dateModified', models.DateTimeField(auto_now=True)),
                ('primaryKey', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('title', models.CharField(default='BlogTitleProvider', max_length=512)),
                ('description', models.CharField(blank=True, max_length=1024, null=True)),
            ],
        ),
    ]
