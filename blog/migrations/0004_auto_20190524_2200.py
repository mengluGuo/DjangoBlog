# Generated by Django 2.2.1 on 2019-05-24 22:00

from django.db import migrations
import froala_editor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20190517_1310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=froala_editor.fields.FroalaField(),
        ),
    ]
