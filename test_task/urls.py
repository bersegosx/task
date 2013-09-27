from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('test_task.views',
    # Examples:
    # url(r'^$', 'test_task.views.home', name='home'),
    # url(r'^test_task/', include('test_task.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    url(r"^$", "index", name="index"),
    url(r"^action/list/$", "link_list", name="list"),
    url(r"^action/show/(?P<link_name>\w{1,10})/$", "show", name="show"),
    url(r"^action/delete/(?P<link_name>\w{1,10})/$", "delete", name="delete"),
    url(r"^(?P<link_name>\w{1,10})$", "go_to"),
)
