# Generated by Django 4.2.5 on 2024-04-07 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0004_alter_blog_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=50)),
                ('message', models.TextField(max_length=5000)),
            ],
        ),
    ]