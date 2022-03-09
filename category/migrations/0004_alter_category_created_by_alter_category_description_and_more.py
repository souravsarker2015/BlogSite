# Generated by Django 4.0.3 on 2022-03-09 20:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('category', '0003_alter_category_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Created By'),
        ),
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.TextField(blank=True, max_length=5000, null=True, verbose_name='Category Descriptions'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=200, unique=True, verbose_name='Category Name'),
        ),
        migrations.AlterField(
            model_name='category',
            name='status',
            field=models.CharField(choices=[('P', 'Pending for approval'), ('R', 'Rejected'), ('A', 'Approved'), ('B', 'Blocked')], default='P', max_length=1, verbose_name='Category Status'),
        ),
    ]
