# Generated by Django 4.1.7 on 2023-04-11 15:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_delete_abc'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staf',
            name='message',
        ),
    ]