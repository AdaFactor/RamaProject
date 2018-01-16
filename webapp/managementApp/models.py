from django.db import models
from django.contrib.postgres.fields import ArrayField


class Address(models.Model):
    house_no = models.CharField(max_length=8)
    village_no = models.CharField(max_length=3)
    alley = models.CharField(max_length=32)
    road = models.CharField(max_length=32)
    area = models.CharField(max_length=32)
    sub_area = models.CharField(max_length=32)
    province = models.CharField(max_length=32)
    post_code = models.CharField(max_length=5)

    def __str__(self):
        return self.province

class Member(models.Model):
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

    def __str__(self):
        return ('%d %s %s') % (self.id, self.first_name, self.last_name)