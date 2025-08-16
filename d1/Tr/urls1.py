"""
URL configuration for d1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path
from django.urls import include
from d1.train.vw_t1 import  test_http
from d1.train.vw_t1 import  test_json
from d1.train.vw_t1 import  test_http1
from website1.views import test_http2

urlpatterns = [
    path('admin/', admin.site.urls),

    #jahantetst1
    path('test_http',test_http),
    path('test_json',test_json),
    path('test_http1',test_http1),
    path('test_http2',test_http2),
    path('website1/',include('website1.urls')),
]
