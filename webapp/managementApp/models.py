from django.db import models
from django.contrib.postgres.fields import ArrayField


class Address(models.Model):
    """
        Address og member in the site.
    """
    house_no = models.CharField(max_length=8)
    village_no = models.CharField(max_length=3)
    alley = models.CharField(max_length=32)
    road = models.CharField(max_length=32)
    area = models.CharField(max_length=32)
    sub_area = models.CharField(max_length=32)
    province = models.CharField(max_length=32)
    post_code = models.CharField(max_length=5)


    def __str__(self):
        return ('%s หมู่ %s ถ.%s ซ.%s อ.%s ต.%s จ.%s %s') % (self.house_no, self.village_no, self.road, self.alley, self.area, self.sub_area, self.province, self.post_code)

1
class Member(models.Model):
    """
        Members of the site are stored in this data model
    """
    prefix_choice = (
        ('Mr', 'นาย'),
        ('Mrs', 'นาง'),
        ('Ms', 'นางสาว'),
    )
    gender_choice = (
        ('m', 'ชาย'),
        ('w', 'หญิง'),
        ('x', 'ไม่ระบุ'),
    )
    prefix = models.CharField(max_length=6, choices=prefix_choice)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    gender = models.CharField(max_length=8, choices=gender_choice)
    citizen_id = models.CharField(max_length=13)
    date_birth = models.DateField()
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    phone_no = ArrayField(
        models.CharField(max_length=10),
        size=3
    )
    email = models.CharField(max_length=128)
    registered_datetime = models.DateTimeField(auto_now=True)
    change_list_template = "admin/change_list_filter_sidebar.html"

    @staticmethod
    def autocomplete_search_fields():
        return ('id_iexact', 'area_icontains', 'sub_area_icontains')


    def __str__(self):
        return ('%d %s %s') % (self.id, self.first_name, self.last_name)

    def related_label(self):
        return u"อ.%s ต.%s" % (self.address.area, self.address.sub_area)
