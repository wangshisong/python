# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class DCategory(models.Model):
    id = models.CharField(primary_key=True, max_length=40)
    category_name = models.CharField(max_length=40, blank=True, null=True)
    book_counts = models.CharField(max_length=40, blank=True, null=True)
    category_pid = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'd_category'


class DOrderltem(models.Model):
    shop_bookid = models.ForeignKey('TBook', models.DO_NOTHING, db_column='shop_bookid', blank=True, null=True)
    shop_ordid = models.ForeignKey('TOrder', models.DO_NOTHING, db_column='shop_ordid', blank=True, null=True)
    shop_num = models.CharField(max_length=40, blank=True, null=True)
    total_price = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'd_orderltem'


class Postbox(models.Model):
    postbox_name = models.CharField(max_length=255, blank=True, null=True)
    code = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'postbox'


class TAddress(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    detail_address = models.CharField(max_length=255, blank=True, null=True)
    zipcode = models.CharField(max_length=255, blank=True, null=True)
    tel_phone = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_address'


class TBook(models.Model):
    book_name = models.CharField(max_length=40, blank=True, null=True)
    book_author = models.CharField(max_length=40, blank=True, null=True)
    book_publish = models.CharField(max_length=40, blank=True, null=True)
    publish_time = models.DateField(blank=True, null=True)
    revision = models.IntegerField(blank=True, null=True)
    book_isbn = models.CharField(max_length=40, blank=True, null=True)
    word_count = models.IntegerField(blank=True, null=True)
    page_count = models.IntegerField(blank=True, null=True)
    open_type = models.CharField(max_length=40, blank=True, null=True)
    book_paper = models.CharField(max_length=40, blank=True, null=True)
    book_wrapper = models.CharField(max_length=40, blank=True, null=True)
    book_category = models.ForeignKey(DCategory, models.DO_NOTHING, db_column='book_category', blank=True, null=True)
    book_price = models.IntegerField(blank=True, null=True)
    book_dprice = models.IntegerField(blank=True, null=True)
    product_image = models.CharField(max_length=255, blank=True, null=True)
    series_name = models.CharField(max_length=20, blank=True, null=True)
    printing_time = models.DateField(blank=True, null=True)
    impression = models.CharField(max_length=20, blank=True, null=True)
    stock = models.CharField(max_length=20, blank=True, null=True)
    shelves_date = models.DateField(blank=True, null=True)
    customer_socre = models.CharField(max_length=40, blank=True, null=True)
    book_status = models.CharField(max_length=40, blank=True, null=True)
    sales = models.CharField(max_length=40, blank=True, null=True)
    book_category_gory = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_book'


class TOrder(models.Model):
    num = models.FloatField(blank=True, null=True)
    create_date = models.DateField(blank=True, null=True)
    price = models.CharField(max_length=20, blank=True, null=True)
    user = models.ForeignKey('TUser', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_order'


class TUser(models.Model):
    user_email = models.CharField(max_length=40, blank=True, null=True)
    user_password = models.TextField(blank=True, null=True)
    user_name = models.CharField(max_length=40, blank=True, null=True)
    user_status = models.CharField(max_length=40, blank=True, null=True)
    password = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_user'
