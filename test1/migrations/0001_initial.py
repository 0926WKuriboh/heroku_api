# Generated by Django 2.2.5 on 2019-09-20 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.TextField(primary_key=True, serialize=False)),
                ('title', models.TextField(blank=True, null=True)),
                ('time', models.TextField(blank=True, null=True)),
                ('link', models.TextField(blank=True, null=True)),
                ('author', models.TextField(blank=True, null=True)),
                ('text', models.TextField(blank=True, null=True)),
                ('images', models.TextField(blank=True, null=True)),
                ('category', models.TextField(blank=True, null=True)),
                ('tag', models.TextField(blank=True, null=True)),
                ('display', models.BooleanField()),
            ],
            options={
                'db_table': 'data',
                'managed': False,
            },
        ),
    ]