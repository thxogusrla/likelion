# Generated by Django 2.1.4 on 2019-05-24 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='published_at',
            field=models.DateTimeField(null=True),
        ),
    ]
