# Generated by Django 3.2.8 on 2023-09-22 17:28

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_question_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='code',
            field=tinymce.models.HTMLField(),
        ),
    ]
