# Generated by Django 4.2 on 2023-04-28 11:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0004_doctype_alter_item_doc_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='doc_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item', to=settings.AUTH_USER_MODEL),
        ),
    ]
