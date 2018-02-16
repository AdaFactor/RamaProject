from django.contrib import admin
from .models import Member, Address


class MemberAdmin(admin.ModelAdmin):
    list_display_links = ('first_name', 'last_name')
    list_display = (
        'id',
        'prefix',
        'first_name',
        'last_name',
        'gender',
        'date_birth',
        'address',
        'phone_no',
        'email',
        'reference_person',
        'paid',
        'expiry_date',
        'registered_datetime'
    )
    list_filter = (
        'gender',
        'address__area',
        'address__sub_area',
        'address__province',
        'paid',
        'expiry_date'
    )
    search_fields = [
        'first_name',
        'last_name',
        'email',
        'phone_no',
        'date_birth',
        'registered_datetime',
        'address__house_no',
        'address__village_no',
        'address__alley',
        'address__road',
        'address__area',
        'address__sub_area',
        'address__province',
        'address__post_code',
    ]
    raw_id_fields = ('address', 'relationship')

    related_lookup_fields = {
        'fk': ['address', ],
    }


class AddressAdmin(admin.ModelAdmin):
    list_display = (
        'house_no',
        'resident_name',
        'village_no',
        'alley',
        'road',
        'area',
        'sub_area',
        'province',
        'post_code',
    )

admin.site.register(Member, MemberAdmin)
admin.site.register(Address, AddressAdmin)