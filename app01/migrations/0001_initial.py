# Generated by Django 2.0.6 on 2019-05-17 06:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DCategory',
            fields=[
                ('id', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('category_name', models.CharField(blank=True, max_length=40, null=True)),
                ('book_counts', models.CharField(blank=True, max_length=40, null=True)),
                ('category_pid', models.CharField(blank=True, max_length=40, null=True)),
            ],
            options={
                'db_table': 'd_category',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DOrderltem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shop_num', models.CharField(blank=True, max_length=40, null=True)),
                ('total_price', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'd_orderltem',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(blank=True, max_length=40, null=True)),
                ('book_author', models.CharField(blank=True, max_length=40, null=True)),
                ('book_publish', models.CharField(blank=True, max_length=40, null=True)),
                ('publish_time', models.DateField(blank=True, null=True)),
                ('revision', models.IntegerField(blank=True, null=True)),
                ('book_isbn', models.CharField(blank=True, max_length=40, null=True)),
                ('word_count', models.IntegerField(blank=True, null=True)),
                ('page_count', models.IntegerField(blank=True, null=True)),
                ('open_type', models.CharField(blank=True, max_length=40, null=True)),
                ('book_paper', models.CharField(blank=True, max_length=40, null=True)),
                ('book_wrapper', models.CharField(blank=True, max_length=40, null=True)),
                ('book_price', models.IntegerField(blank=True, null=True)),
                ('book_dprice', models.IntegerField(blank=True, null=True)),
                ('product_image', models.CharField(blank=True, max_length=255, null=True)),
                ('series_name', models.CharField(blank=True, max_length=20, null=True)),
                ('printing_time', models.DateField(blank=True, null=True)),
                ('impression', models.CharField(blank=True, max_length=20, null=True)),
                ('stock', models.CharField(blank=True, max_length=20, null=True)),
                ('shelves_date', models.DateField(blank=True, null=True)),
                ('customer_socre', models.CharField(blank=True, max_length=40, null=True)),
                ('book_status', models.CharField(blank=True, max_length=40, null=True)),
                ('sales', models.CharField(blank=True, max_length=40, null=True)),
            ],
            options={
                'db_table': 't_book',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.FloatField(blank=True, null=True)),
                ('create_date', models.DateField(blank=True, null=True)),
                ('price', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 't_order',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_email', models.CharField(blank=True, max_length=40, null=True)),
                ('user_password', models.CharField(blank=True, max_length=40, null=True)),
                ('user_name', models.CharField(blank=True, max_length=40, null=True)),
                ('user_status', models.CharField(blank=True, max_length=40, null=True)),
            ],
            options={
                'db_table': 't_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TAddress',
            fields=[
                ('id', models.ForeignKey(db_column='id', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='app01.TOrder')),
                ('name', models.CharField(blank=True, max_length=40, null=True)),
                ('detail_address', models.CharField(blank=True, max_length=40, null=True)),
                ('zipcode', models.CharField(blank=True, max_length=6, null=True)),
                ('tel_phone', models.CharField(blank=True, max_length=40, null=True)),
                ('phone', models.CharField(blank=True, max_length=40, null=True)),
            ],
            options={
                'db_table': 't_address',
                'managed': False,
            },
        ),
    ]
