# Generated by Django 2.2.5 on 2019-10-10 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('year', models.IntegerField(default=1950)),
            ],
            options={
                'db_table': 'cars',
            },
        ),
    ]
