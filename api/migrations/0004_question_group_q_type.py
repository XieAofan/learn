# Generated by Django 4.1.2 on 2023-04-16 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_question_img_alter_question_group_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='question_group',
            name='q_type',
            field=models.CharField(choices=[('s', '单选'), ('i', '不定项'), ('m', '多媒体')], default='i', max_length=10),
        ),
    ]
