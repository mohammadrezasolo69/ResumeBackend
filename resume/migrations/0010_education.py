# Generated by Django 3.2 on 2022-06-07 08:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0009_auto_20220607_1228'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.IntegerField(blank=True, choices=[(0, 'Cycle'), (1, 'Diploma'), (2, 'Bachelor'), (3, 'Master'), (4, 'Doctorate'), (5, 'University'), (6, 'Student')], max_length=1, verbose_name='Grade')),
                ('major', models.CharField(blank=True, max_length=200, verbose_name='Major')),
                ('start_date', models.DateTimeField(blank=True, verbose_name='Start')),
                ('end_date', models.DateTimeField(blank=True, verbose_name='End')),
                ('resume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='education', to='resume.resume', verbose_name='Resume')),
            ],
        ),
    ]
