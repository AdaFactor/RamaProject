from django.contrib import admin
from .models import Member, Address


class MemberAdmin(admin.ModelAdmin):
    list_display_links = ('first_name', 'last_name')
    list_display = ('prefix', 'first_name', 'last_name', 'gender', 'date_birth', 'address', 'phone_no', 'email', 'registered_datetime')
    list_filter = ('gender',)

class AddressAdmin(admin.ModelAdmin):
    list_display = ('house_no', 'village_no', 'alley', 'road', 'area', 'sub_area', 'province', 'post_code')

admin.site.register(Member, MemberAdmin)
admin.site.register(Address, AddressAdmin)
