# Generated by Django 3.0.9 on 2020-08-04 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20200804_1930'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='snippet',
            field=models.CharField(default='Add a snippet', max_length=150),
        ),
    ]
