# Generated by Django 4.2 on 2023-04-26 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='doc_type',
            field=models.TextField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
