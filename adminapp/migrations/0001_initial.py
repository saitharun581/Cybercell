# Generated by Django 3.2.7 on 2022-07-07 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdminAddInformerModel',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('area', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100, null=True)),
                ('password', models.CharField(max_length=100, null=True)),
                ('image', models.ImageField(null=True, upload_to='images/')),
            ],
            options={
                'db_table': 'add_informer',
            },
        ),
        migrations.CreateModel(
            name='AdminAddPoliceModel',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('area', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100, null=True)),
                ('password', models.CharField(max_length=100, null=True)),
                ('image', models.ImageField(null=True, upload_to='images/')),
            ],
            options={
                'db_table': 'add_police',
            },
        ),
    ]
