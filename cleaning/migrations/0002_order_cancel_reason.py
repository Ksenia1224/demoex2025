# Generated by Django 5.2.3 on 2025-06-19 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cleaning', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='cancel_reason',
            field=models.TextField(blank=True, null=True, verbose_name='Причина отмены'),
        ),
    ]
