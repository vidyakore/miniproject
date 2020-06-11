# Generated by Django 3.0.5 on 2020-06-10 17:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('formsa', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25, null=True)),
                ('text', models.TextField(default='  ', null=True)),
                ('author', models.CharField(default='  ', max_length=50, null=True)),
                ('sub_heading', models.CharField(default='  ', max_length=50, null=True)),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('photo', models.ImageField(blank=True, default=' ', null='', upload_to='img/user.Username/%Y/%m/%d/')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(blank=True, max_length=50)),
                ('first_name', models.CharField(blank=True, max_length=50)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='images/profile/%Y/%m/%d/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(upload_to='')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='regi',
        ),
    ]
