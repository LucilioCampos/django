from django.contrib import admin

from core.models import Usuario, Address, Team, License, Workflow, Kind, Kanban, Company

admin.site.register(Usuario)
admin.site.register(Address)
admin.site.register(Team)
admin.site.register(License)
admin.site.register(Workflow)
admin.site.register(Kind)
admin.site.register(Kanban)
admin.site.register(Company)
