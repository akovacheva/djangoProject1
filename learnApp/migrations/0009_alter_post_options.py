# Generated by Django 3.2.15 on 2022-09-29 21:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learnApp', '0008_alter_post_date_created_alter_post_last_modified'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-date_created']},
        ),
    ]