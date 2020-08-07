"""myblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
import post.views
import portfolio.views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', post.views.home, name="index"),
    path('post/<int:post_id>/', post.views.post_detail, name="post_detail"),     
    #url(r'^posts/(?P<post_id>[0-9]+)/$', views.post_detail), ## Its old version format
    path('portfolio/', portfolio.views.portfolio_detail_page, name="portfolio_detail_page"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
