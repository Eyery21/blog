# Generated by Django 5.0.6 on 2024-06-04 21:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_project_new'),
    ]

    operations = [
        migrations.CreateModel(
            name='Framwork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='project',
            name='category',
        ),
        migrations.RemoveField(
            model_name='project',
            name='technologies',
        ),
        migrations.AddField(
            model_name='project',
            name='language',
            field=models.CharField(choices=[('HTML/CSS', 'HTML/CSS'), ('PHP', 'PHP'), ('JS', 'JavaScript'), ('PYTHON', 'Python')], default=0, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='framework',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='projects', to='blog.framwork'),
        ),
    ]
