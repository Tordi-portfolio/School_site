# Generated by Django 5.2.1 on 2025-05-27 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='result',
            old_name='agric',
            new_name='agric_exam',
        ),
        migrations.RenameField(
            model_name='result',
            old_name='civic',
            new_name='agric_test1',
        ),
        migrations.RenameField(
            model_name='result',
            old_name='computer',
            new_name='agric_test2',
        ),
        migrations.RenameField(
            model_name='result',
            old_name='crs',
            new_name='civic_exam',
        ),
        migrations.RenameField(
            model_name='result',
            old_name='english',
            new_name='civic_test1',
        ),
        migrations.RenameField(
            model_name='result',
            old_name='government',
            new_name='civic_test2',
        ),
        migrations.RenameField(
            model_name='result',
            old_name='maths',
            new_name='computer_exam',
        ),
        migrations.RenameField(
            model_name='result',
            old_name='quantitative',
            new_name='computer_test1',
        ),
        migrations.RenameField(
            model_name='result',
            old_name='social_studies',
            new_name='computer_test2',
        ),
        migrations.RenameField(
            model_name='result',
            old_name='verbal_reasoning',
            new_name='crs_exam',
        ),
        migrations.AddField(
            model_name='result',
            name='crs_test1',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='result',
            name='crs_test2',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='result',
            name='english_exam',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='result',
            name='english_test1',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='result',
            name='english_test2',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='result',
            name='government_exam',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='result',
            name='government_test1',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='result',
            name='government_test2',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='result',
            name='maths_exam',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='result',
            name='maths_test1',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='result',
            name='maths_test2',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='result',
            name='quantitative_exam',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='result',
            name='quantitative_test1',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='result',
            name='quantitative_test2',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='result',
            name='social_studies_exam',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='result',
            name='social_studies_test1',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='result',
            name='social_studies_test2',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='result',
            name='verbal_reasoning_exam',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='result',
            name='verbal_reasoning_test1',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='result',
            name='verbal_reasoning_test2',
            field=models.IntegerField(default=0),
        ),
    ]
