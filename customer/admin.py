from optparse import Option
from django.contrib import admin
from .models import Choice, Options, Question, Userans, detail, order, payment,register
# Register your models here.

admin.site.register(register)
admin.site.register(detail)
admin.site.register(order)
admin.site.register(payment)
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Userans)
admin.site.register(Options)
