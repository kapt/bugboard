# Generated by Django 2.2.6 on 2019-10-16 10:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bugboard', '0006_auto_20191016_1053'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id_comment', models.IntegerField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField()),
                ('text', models.TextField(null=True)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bugboard.Member')),
            ],
        ),
    ]
