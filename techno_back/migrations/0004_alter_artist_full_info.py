# Generated by Django 4.1.1 on 2023-05-29 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('techno_back', '0003_artist_full_info'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='full_info',
            field=models.TextField(help_text='Повне інфо артиста', max_length=2000),
        ),
    ]
