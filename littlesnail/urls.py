from django.conf.urls import patterns, include, url
from views import handleRequest
# from views import  score_task
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns( '',
    # Examples:
    url( r'^', handleRequest ),
#     url( r'^grade/task/score/$', score_task ),
    # url(r'^littlesnail/', include('littlesnail.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
 )
