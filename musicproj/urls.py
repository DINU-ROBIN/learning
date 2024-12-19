"""
URL configuration for musicproj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path,include
from home import views as viewshome
from createacc import views as createviews

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",viewshome.home, name="home"), 
    path("login/",createviews.login_view,name="login"),
    path("create/",createviews.createacc , name="create"),
    path("forgot/",createviews.forgot, name="forgot"),
    path("update/",createviews.updatepassword,name="update"),
    path("updatepassword/<str:username>/",createviews.updatepassword,name="updatepassword"),
    # path("content",content.conthome,name="contentt")
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)