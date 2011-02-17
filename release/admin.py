from djangit.release.models import Server, Repo, Branch
from django.contrib import admin

admin.site.register(Server)
admin.site.register(Repo)
admin.site.register(Branch)