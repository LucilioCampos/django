from django.contrib import admin

from usuarios.models.address import Address
from usuarios.models.kind import Kind
from usuarios.models.license import License
from usuarios.models.team import Team
from usuarios.models.usuario import Usuario

admin.site.register(Usuario)
admin.site.register(Address)
admin.site.register(Kind)
admin.site.register(License)
admin.site.register(Team)


