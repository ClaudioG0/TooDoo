from django.contrib import admin
from django.urls import path
from .views import index, results
from users.views import login_view, register_view, logout_view

from django.conf.urls.static import static
from django.conf import settings


app_name = "toodoo"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('accounts/login/', login_view, name='login'),
    path('accounts/register/', register_view, name='register'),
    path('accounts/logout/', logout_view, name='logout'),
    path('<int:list_id>/results/', results, name="results"),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
