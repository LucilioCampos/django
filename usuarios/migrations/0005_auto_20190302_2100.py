# Generated by Django 2.1.7 on 2019-03-03 00:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0004_auto_20190302_2059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='create_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 3, 2, 21, 0, 24, 921800)),
        ),
        migrations.AlterField(
            model_name='address',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 3, 2, 21, 0, 24, 921800)),
        ),
        migrations.AlterField(
            model_name='company',
            name='create_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 3, 2, 21, 0, 24, 923799)),
        ),
        migrations.AlterField(
            model_name='company',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 3, 2, 21, 0, 24, 923799)),
        ),
        migrations.AlterField(
            model_name='kanban',
            name='create_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 3, 2, 21, 0, 24, 923799)),
        ),
        migrations.AlterField(
            model_name='kanban',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 3, 2, 21, 0, 24, 923799)),
        ),
        migrations.AlterField(
            model_name='kind',
            name='create_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 3, 2, 21, 0, 24, 924800)),
        ),
        migrations.AlterField(
            model_name='kind',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 3, 2, 21, 0, 24, 924800)),
        ),
        migrations.AlterField(
            model_name='team',
            name='create_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 3, 2, 21, 0, 24, 922799)),
        ),
        migrations.AlterField(
            model_name='team',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 3, 2, 21, 0, 24, 922799)),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='create_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 3, 2, 21, 0, 24, 922799)),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 3, 2, 21, 0, 24, 922799)),
        ),
        migrations.AlterField(
            model_name='workflow',
            name='create_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 3, 2, 21, 0, 24, 924800)),
        ),
        migrations.AlterField(
            model_name='workflow',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 3, 2, 21, 0, 24, 924800)),
        ),
    ]
