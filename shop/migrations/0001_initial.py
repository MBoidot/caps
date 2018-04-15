# Generated by Django 2.0.2 on 2018-04-15 03:07

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='shop_item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_type', models.CharField(max_length=255)),
                ('user_designed', models.BooleanField()),
                ('designer_designed', models.BooleanField()),
                ('designer_name', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('level', models.IntegerField()),
                ('name', models.CharField(max_length=255)),
                ('serie', models.CharField(max_length=255)),
                ('classification', models.CharField(max_length=255)),
                ('date_released', models.DateField()),
                ('mod_files', models.FileField(upload_to='')),
                ('event_related', models.BooleanField()),
                ('event_name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('user_fk', models.ForeignKey(on_delete='CASCADE', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
