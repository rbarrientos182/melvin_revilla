from django.contrib import admin
from .models import Member

class MemberAdmin(admin.ModelAdmin):
    model = Member
    list_display = ('id', 'name', 'email', 'joined_date')
    search_fields = ('name', 'email')
    list_filter = ('joined_date',)

admin.site.register(Member, MemberAdmin)
admin.site.site_header = "Members Admin"
admin.site.site_title = "Members Admin Portal"
admin.site.index_title = "Bienvenido al Portal Administrativo de Miembros"

