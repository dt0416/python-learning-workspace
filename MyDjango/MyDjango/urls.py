from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()
import blog.views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'MyDjango.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    
    # url(r'blog/index/$', 'blog.views.index'), # same with next line
    url(r'blog/index/$', blog.views.index), # must import
    
    url(r'blog/employee/$', blog.views.employee),
    url(r'blog/book/$', blog.views.book),
    url(r'blog/register/$', blog.views.register),
)
