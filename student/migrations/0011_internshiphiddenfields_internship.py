# Generated by Django 3.0.5 on 2020-06-08 22:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0010_internshiphiddenfields'),
    ]

    operations = [
        migrations.AddField(
            model_name='internshiphiddenfields',
            name='internship',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='student.InternShip'),
            preserve_default=False,
        ),
    ]
