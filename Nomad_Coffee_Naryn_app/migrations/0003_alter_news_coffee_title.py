# Generated by Django 4.0.4 on 2022-05-25 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Nomad_Coffee_Naryn_app', '0002_news_coffee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news_coffee',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Заголовок'),
        ),
    ]
