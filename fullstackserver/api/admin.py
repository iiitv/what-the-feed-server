from django.contrib import admin
from .models import *

admin.site.register(User)
admin.site.register(Link)
admin.site.register(SearchString)
admin.site.register(Cache)