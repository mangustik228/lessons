from django.contrib import admin
from . import models as M


# Register your models here.


admin.site.register(M.Article)
admin.site.register(M.Journalist)
