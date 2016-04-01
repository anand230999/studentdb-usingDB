from django.conf.urls import patterns, url
from studentdb import views

urlpatterns = patterns('',
        url(r'^$',views.index, name='index'),
        url(r'^view/$',views.view, name='view'),
        url(r'^add/$',views.add, name='add'),
        url(r'^delete/$',views.delete, name='delete'),
#        url(r'^modify/$',views.modify, name='modify'),
        url(r'^search/$',views.search, name='search'),
        url(r'^register/$',views.register, name='register'),
        url(r'^login/$', views.user_login, name='login'),
        url(r'^logout/$', views.user_logout, name='logout'),
)
