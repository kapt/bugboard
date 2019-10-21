# Generated by Django 2.2.6 on 2019-10-16 12:02

# Third party
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bugboard', '0009_auto_20191016_1332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='member',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bugboard.Member'),
        ),
        migrations.AlterField(
            model_name='member',
            name='avatar_url',
            field=models.URLField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]
