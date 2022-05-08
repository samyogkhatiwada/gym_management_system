from django.contrib import admin
from .models import Member, Payment, Trainer
# Register your models here.
admin.site.register(Member)
@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
 list_filter = 'member', 'date'
 search_fields = 'member', 'date'

 admin.site.register(Trainer)