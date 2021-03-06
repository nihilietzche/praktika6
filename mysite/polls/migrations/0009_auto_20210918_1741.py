# Generated by Django 3.2.6 on 2021-09-18 14:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0008_auto_20210916_2038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='max_points',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='result',
            name='title',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='polls.test'),
        ),
    ]
