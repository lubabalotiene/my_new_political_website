# Generated by Django 5.0.4 on 2024-05-20 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_new_combrate', '0004_biography_communityinvolvement_loginbutton_person_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyNewCombrateRegistrationLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='registrationlink',
            name='button_text',
            field=models.CharField(default='Register Now', max_length=50),
        ),
        migrations.AddField(
            model_name='registrationlink',
            name='url',
            field=models.URLField(default=4),
            preserve_default=False,
        ),
    ]
