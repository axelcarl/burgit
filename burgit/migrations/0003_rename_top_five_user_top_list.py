# Generated by Django 4.1.4 on 2022-12-28 16:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('burgit', '0002_burgerplace_toplist_user_top_five'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='top_five',
            new_name='top_list',
        ),
    ]