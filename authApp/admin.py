from django.contrib import admin
from .models.user import User
from .models.account import Account
from .models.products import Producto
from .models.shoppinghistory import HistorialdeCompras
from .models.tokens import Tokens


admin.site.register(User)
admin.site.register(Account)
admin.site.register(Producto)
admin.site.register(HistorialdeCompras)
admin.site.register(Tokens)
# Register your models here.
