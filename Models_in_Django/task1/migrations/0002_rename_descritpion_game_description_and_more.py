# Generated by Django 4.2.16 on 2024-11-24 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task1', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='descritpion',
            new_name='description',
        ),
        migrations.RemoveField(
            model_name='game',
            name='BooleanField',
        ),
        migrations.RemoveField(
            model_name='game',
            name='DecimalField',
        ),
        migrations.AlterField(
            model_name='buyer',
            name='name',
            field=models.CharField(max_length=15, verbose_name='username'),
        ),
        migrations.AlterField(
            model_name='game',
            name='cost',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
        migrations.AlterField(
            model_name='game',
            name='size',
            field=models.DecimalField(decimal_places=4, max_digits=20),
        ),
    ]
