# Generated by Django 2.2 on 2020-06-03 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20200603_1507'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='feature',
            field=models.CharField(choices=[('True', 'True'), ('False', 'False')], default=True, max_length=100, verbose_name='Features'),
            preserve_default=False,
        ),
    ]
