# Generated by Django 5.0.4 on 2024-05-12 19:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_new_combrate', '0003_yourmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Biography',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='CommunityInvolvement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='LoginButton',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('button_text', models.CharField(default='Log In', max_length=50)),
                ('url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='PoliticalBeliefs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('person', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='political_beliefs', to='my_new_combrate.person')),
            ],
        ),
        migrations.CreateModel(
            name='RegistrationLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link_text', models.CharField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='my_new_combrate',
            name='supporters',
        ),
        migrations.DeleteModel(
            name='YourModel',
        ),
        migrations.AddField(
            model_name='communityinvolvement',
            name='person',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='community_involvement', to='my_new_combrate.person'),
        ),
        migrations.AddField(
            model_name='biography',
            name='person',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='biography', to='my_new_combrate.person'),
        ),
        migrations.DeleteModel(
            name='my_new_combrate',
        ),
        migrations.DeleteModel(
            name='Supporter',
        ),
    ]
