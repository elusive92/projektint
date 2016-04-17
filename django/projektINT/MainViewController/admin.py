from django.contrib import admin

# Register your models here.
from .models import MainViewController

class MainViewControllerAdmin(admin.ModelAdmin):
    class Meta:
        model = MainViewController
        
admin.site.register(MainViewController, MainViewControllerAdmin)