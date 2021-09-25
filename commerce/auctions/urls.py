from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("watch_list",views.watch_list, name = "watch_list"),
    path("product/<str:item>", views.product, name="product")
]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)