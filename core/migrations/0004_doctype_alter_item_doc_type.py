# Generated by Django 4.2 on 2023-04-28 11:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_item_doc_link_alter_item_doc_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctype',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='item',
            name='doc_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='item', to='core.doctype'),
            preserve_default=False,
        ),
    ]
