# Generated by Django 3.2.9 on 2022-02-27 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sendmail', '0002_auto_20220227_2010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermail',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]