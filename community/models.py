# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models
from datetime import datetime

class Area(models.Model):
    # id = models.IntegerField(null=True, primary_key=True, blank=True)
    url = models.TextField(null=False, blank=False)             # 区域anjuke的url http://beijing.anjuke.com/v2/community/list/<url>
    name = models.TextField(null=False, blank=False)            # 区域名 (朝阳, 海淀等)
    community = models.IntegerField(null=False, blank=False)    # 区域内小区个数
    class Meta:
        db_table = u'area'

class CommunityInfo(models.Model):
    # id = models.IntegerField(null=True, primary_key=True, blank=True)
    url = models.IntegerField(null=False, blank=False)          # 小区anjuke的url, 在anjuke中也是一个唯一的ID http://beijing.anjuke.com/v2/community/view/<url>
    name = models.TextField(null=False, blank=False)            # 小区name
    latitude = models.DecimalField(null=True, blank=True, max_digits=18, decimal_places=15)
    longitude = models.DecimalField(null=True, blank=True, max_digits=18, decimal_places=15)
    location = models.TextField(null=True, blank=True)          # 中文地址
    sale_trends = models.TextField(null=True, blank=True)       # 价格趋势, anjuke的url http://beijing.anjuke.com/v2/community/trends/<sale_trends>
    rental_trends = models.TextField(null=True, blank=True)     # 租金趋势, anjuke的url http://beijing.haozu.com/compound/trends/<rental_trends>
    houses = models.IntegerField(null=True, blank=True)         # 小区总户数
    pack = models.TextField(null=True, blank=True)              # 小区停车位个数
    developer = models.TextField(null=True, blank=True)         # 开发商
    tenement = models.TextField(null=True, blank=True)          # 物业公司
    tenement_type = models.TextField(null=True, blank=True)     # 物业类型 (公寓, 别墅等)
    building_date = models.DateField(null=True, blank=True)     # 竣工日期
    plot_ratio = models.DecimalField(null=True, blank=True, max_digits=6, decimal_places=3)     # 容积率
    afforest = models.DecimalField(null=True, blank=True, max_digits=6, decimal_places=3)       # 绿化率
    area = models.TextField(null=False, blank=False)                                            # 所属区域
    timestamp = models.DateTimeField(auto_now=True, auto_now_add=True)                          # 数据更新时间戳
    class Meta:
        db_table = u'community_info'

class CommunityPrice(models.Model):
    # id = models.IntegerField(null=True, primary_key=True, blank=True)
    info = models.ForeignKey(CommunityInfo)
    price = models.IntegerField(null=True, blank=True)          # 当前平均售价 元/平米
    sales = models.IntegerField(null=True, blank=True)          # 当前出售房源
    sale_1 = models.IntegerField(null=True, blank=True)         # 一室出售房源
    sale_2 = models.IntegerField(null=True, blank=True)         # 二室出售房源
    sale_3 = models.IntegerField(null=True, blank=True)         # 三室出售房源
    sale_4 = models.IntegerField(null=True, blank=True)         # 四室出售房源
    sale_5 = models.IntegerField(null=True, blank=True)         # 五室出售房源
    sale_6 = models.IntegerField(null=True, blank=True)         # 五室以上出售房源
    rental = models.IntegerField(null=True, blank=True)         # 当前平均租金 元/套
    rents = models.IntegerField(null=True, blank=True)          # 当前出租房源
    timestamp = models.DateTimeField(auto_now=True, auto_now_add=True)      # 数据创建时间戳
    class Meta:
        db_table = u'community_price'



class statisticsManager(models.Manager):
    





class PriceStatistics(models.Model):
    info = models.ForeignKey(CommunityPrice)
    price_order = models.IntegerField(null=True, blank=True)
    rental_order = models.IntegerField(null=True, blank=True)
    price_rental_ratio = models.FloatField(null=True, blank=True)
    price_rental_order = models.FloatField(null=True, blank=True)
    sales_order = models.IntegerField(null=True, blank=True)
    rents_order = models.IntegerField(null=True, blank=True)

    create = statisticsManager()

    class Meta:
        db_table = u'community_price'

