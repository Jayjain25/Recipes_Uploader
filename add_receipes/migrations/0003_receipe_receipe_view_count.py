# Generated by Django 4.2.3 on 2023-07-28 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('add_receipes', '0002_receipe_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='receipe',
            name='receipe_view_count',
            field=models.IntegerField(default=1),
        ),
    ]
