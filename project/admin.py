from django.contrib import admin

from .models import *

admin.site.register(Portfolio)
admin.site.register(Position)
admin.site.register(Person)
admin.site.register(Project)
admin.site.register(Task)
admin.site.register(Widget)