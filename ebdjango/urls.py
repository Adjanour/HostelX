"""ebdjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path
from tasks import views

urlpatterns = [
     path('', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='tasks/login.html'), name='login'),
    path('index/', views.index, name='index'),
    path('add_task/', views.add_task, name='add_task'),
    path('complete_task/<int:task_id>/', views.complete_task, name='complete_task'),
    path('incomplete_task/<int:task_id>/', views.incomplete_task, name='incomplete_task'),
    path('delete_task/<int:task_id>/', views.delete_task, name='delete_task'),
]

# urlpatterns = [
#    url(r'^admin/', admin.site.urls),
#    url(r'^', include('helloworld.urls')), 
# ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
