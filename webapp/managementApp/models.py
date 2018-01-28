from django.db import models
from django.contrib.postgres.fields import ArrayField


class Address(models.Model):
    """
        Address og member in the site.
    """
    house_no = models.CharField(max_length=8)
    resident_name = models.CharField(max_length=64, blank=True, null=True)
    village_no = models.CharField(max_length=3)
    alley = models.CharField(max_length=32)
    road = models.CharField(max_length=32)
    area = models.CharField(max_length=32)
    sub_area = models.CharField(max_length=32)
    province = models.CharField(max_length=32)
    post_code = models.CharField(max_length=5)

    def __unicode__(self):
        return u"%s" % (self.house_no)

    def __str__(self):
        return ('%s %s หมู่ %s ถ.%s ซ.%s อ.%s ต.%s จ.%s %s') % (self.house_no, self.resident_name, self.village_no, self.road, self.alley, self.area, self.sub_area, self.province, self.post_code)


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
    reference_person = models.ForeignKey(
        'self',
        related_name='reference_persons',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    relationship = models.ManyToManyField('self', blank=True)
    paid = models.BooleanField(default=False)
    paid_date = models.DateField(blank=True, null=True)
    expiry_date = models.DateField(blank=True, null=True)
    registered_datetime = models.DateTimeField(auto_now=True)
    change_list_template = "admin/change_list_filter_sidebar.html"

    @staticmethod
    def autocomplete_search_fields():
        return ('id_iexact', 'area_icontains', 'sub_area_icontains')

    def __unicode__(self):
        return u"%s %s" % (self.first_name, self.last_name)

    def __str__(self):
        return ('%d %s %s') % (self.id, self.first_name, self.last_name)

    def related_label(self):
        return u"อ.%s ต.%s" % (self.address.area, self.address.sub_area)
