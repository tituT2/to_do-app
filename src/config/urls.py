"""todo_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from user import views as user_view
from django.contrib.auth import views as auth
from todo import views
from django.conf import settings
from django.conf.urls.static import static


################admin setting####################
admin.site.site_header = "Admin Pannel"
admin.site.site_title = "Todo admin"
admin.site.index_title = "Welcome To Administration"
admin.empty_value_display = "**Empty**"

################################################


urlpatterns = [
    #####################home_page###########################################
    path("", views.index, name="todo"),
    ####################give id no. item_id name or item_id=i.id ############
    path("del/<int:item_id>", views.remove, name="del"),
    path("admin/", admin.site.urls),
    #####user related path##########################
    path("login/", user_view.Login, name="login"),
    path(
        "logout/",
        auth.LogoutView.as_view(template_name="todo/index.html"),
        name="logout",
    ),
    path("register/", user_view.register, name="register"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
