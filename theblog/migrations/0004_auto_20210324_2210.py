# Generated by Django 3.1.7 on 2021-03-24 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0003_auto_20210324_1618'),
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(default='coding', max_length=255),
        ),
    ]
