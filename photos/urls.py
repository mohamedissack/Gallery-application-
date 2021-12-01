from django.conf.urls import url
from . import views
from django.contrib import admin

urlpatterns=[
   url('^$',views.home,name = 'home'),
   url('admin/', admin.site.urls),
   url('^search/$',views.search_results,name='search_results'),
]