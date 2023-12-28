from django.contrib import admin
from cmdb import models

# Register your models here.

admin_register_models = [
    models.BookInfo,
    models.Best_seller,
    models.hot_search,
    models.UserModel,
    models.MyCollect,
    models.Score
]

for model in admin_register_models:
    admin.site.register(model)
    