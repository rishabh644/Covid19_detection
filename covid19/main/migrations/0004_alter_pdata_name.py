# Generated by Django 3.2.6 on 2021-09-05 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20210905_0752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pdata',
            name='name',
            field=models.CharField(default='krishna', max_length=200, null=True),
        ),
    ]
