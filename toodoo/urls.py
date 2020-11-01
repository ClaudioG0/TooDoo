from django.contrib import admin
from django.urls import path
from .views import index, add_new_list_view
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
    path('list/<int:pk_group>', add_new_list_view,
         name='add_new_list')

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
