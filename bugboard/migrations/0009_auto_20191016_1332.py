# Generated by Django 2.2.6 on 2019-10-16 11:32

# Third party
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("bugboard", "0008_task_comments")]

    operations = [
        migrations.RenameField(
            model_name="task", old_name="comments", new_name="comment"
        )
    ]
