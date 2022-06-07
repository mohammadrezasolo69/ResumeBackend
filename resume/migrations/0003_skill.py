# Generated by Django 3.2 on 2022-06-07 07:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0002_auto_20220607_1151'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('level', models.IntegerField(choices=[(0, 'Excellent'), (1, 'Good'), (2, 'Medium'), (3, 'Weak')], max_length=1, verbose_name='Level')),
                ('resume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='skills', to='resume.resume', verbose_name='Skill')),
            ],
        ),
    ]