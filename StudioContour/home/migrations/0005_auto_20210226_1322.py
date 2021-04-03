# Generated by Django 3.1.6 on 2021-02-26 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_delete_banner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='project',
            name='start_date',
        ),
        migrations.AlterField(
            model_name='project',
            name='category',
            field=models.CharField(choices=[('0', 'Residential'), ('1', 'Commercial'), ('2', 'Institutional'), ('3', 'Others')], max_length=1, verbose_name='Project category'),
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='projectimage',
            name='category',
            field=models.CharField(choices=[('0', 'Indoor'), ('1', 'Outdoor'), ('2', 'Top view')], max_length=1, verbose_name='Image category'),
        ),
    ]