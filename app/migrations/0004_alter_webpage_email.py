# Generated by Django 4.2.7 on 2023-12-14 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_accessrecord'),
    ]

    operations = [
        migrations.AlterField(
            model_name='webpage',
            name='email',
            field=models.EmailField(default='email2027@gmail.com', max_length=100),
        ),
    ]
