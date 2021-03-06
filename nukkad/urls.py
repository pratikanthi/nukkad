"""nukkad URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2,. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,patterns,include
from django.contrib import admin
from product import views as product_views
import nukkad.settings as settings

admin.site.site_header = settings.ADMIN_SITE_HEADER

urlpatterns = [
    url(r'^$',product_views.index),

    url(r'^admin/', admin.site.urls),
    url(r'^admin', admin.site.urls),

    url(r'^(?P<slug>[\w\-]+)/?$',product_views.get_product),

    url(r'^photologue/', include('photologue.urls', namespace='photologue')),
    url(r'media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT,})

]
