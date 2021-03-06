# Generated by Django 3.2.6 on 2021-09-07 17:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question_point',
            field=models.IntegerField(default=1),
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.TextField()),
                ('choice_point', models.IntegerField(default=0)),
                ('choice', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='polls.question')),
            ],
        ),
    ]
