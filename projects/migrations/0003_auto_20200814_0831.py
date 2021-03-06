# Generated by Django 3.1 on 2020-08-14 08:31

from django.db import migrations, models
import django.db.models.deletion
import projects.models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20200814_0820'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='thum',
            field=models.ImageField(upload_to=projects.models.upload_location),
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to=projects.models.upload_location)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.project')),
            ],
        ),
    ]
