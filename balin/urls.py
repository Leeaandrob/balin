from django.conf.urls import patterns, include, url

urlpatterns = patterns(
    '',
    # url(r'^$', 'balin.views.home', name='home'),
    url(r'', include('balin.auth_balin.urls', namespace='auth_balin')),
)
