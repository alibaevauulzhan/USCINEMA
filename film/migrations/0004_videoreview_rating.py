# Generated by Django 3.2.7 on 2022-02-03 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('film', '0003_auto_20220203_1516'),
    ]

    operations = [
        migrations.AddField(
            model_name='videoreview',
            name='rating',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
