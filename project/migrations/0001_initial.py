# Generated by Django 4.0.4 on 2022-05-21 06:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=100)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.person')),
                ('portfolio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.portfolio')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('status', models.CharField(choices=[('1', 'NEW'), ('2', 'OPEN'), ('3', 'RESOLVED'), ('4', 'COLSED'), ('5', 'IN PROGRESS')], default='1', max_length=333)),
                ('description', models.CharField(max_length=30)),
                ('date', models.DateField(auto_now_add=True)),
                ('dead_line', models.DateField(auto_now_add=True)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.person')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.project')),
            ],
        ),
        migrations.CreateModel(
            name='Widget',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('tache', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.task')),
            ],
        ),
        migrations.AddField(
            model_name='person',
            name='position',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='project.position'),
        ),
    ]
