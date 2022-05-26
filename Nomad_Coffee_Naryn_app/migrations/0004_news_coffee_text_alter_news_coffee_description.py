# Generated by Django 4.0.4 on 2022-05-25 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Nomad_Coffee_Naryn_app', '0003_alter_news_coffee_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='news_coffee',
            name='text',
            field=models.TextField(blank=True, verbose_name='Текст'),
        ),
        migrations.AlterField(
            model_name='news_coffee',
            name='description',
            field=models.CharField(blank=True, max_length=200, verbose_name='Описание'),
        ),
    ]
