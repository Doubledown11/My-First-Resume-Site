# Generated by Django 4.1.5 on 2023-05-17 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0003_blog_entry_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='updated_date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
