# Generated by Django 4.2 on 2023-04-13 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('q_id', models.AutoField(primary_key=True, serialize=False)),
                ('q_type', models.CharField(choices=[('单选', 's'), ('不定项', 'i'), ('多媒体', 'm')], default='不定项', max_length=10)),
                ('ac_data', models.JSONField(null=True)),
                ('choice', models.JSONField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Question_Group',
            fields=[
                ('img', models.CharField(max_length=20)),
                ('question_ids', models.JSONField(null=True)),
                ('ac_data', models.JSONField(null=True)),
                ('qg_id', models.AutoField(primary_key=True, serialize=False)),
                ('subject', models.CharField(choices=[('地理', 'g'), ('地球科学', 'e')], default='地球科学', max_length=10)),
            ],
        ),
    ]
