# Generated by Django 4.0.5 on 2022-06-25 06:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scraper', '0003_keywords_urls_delete_urlkeywords_keywords_url_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='keywords',
            old_name='url_id',
            new_name='url',
        ),
    ]
