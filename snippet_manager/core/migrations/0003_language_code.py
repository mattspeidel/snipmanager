# Generated by Django 2.2.3 on 2019-07-17 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_snippet_original'),
    ]

    operations = [
        migrations.AddField(
            model_name='language',
            name='code',
            field=models.CharField(help_text='code used with prism', max_length=10, null=True),
        ),
    ]