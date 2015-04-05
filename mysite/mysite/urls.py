from django.conf.urls import patterns, include, url
from django.contrib import admin
from django import views
from django.views.generic import TemplateView

# urlpatterns = patterns('',
#     url(r'', include('polls.urls')),
#     url(r'^polls/', include('polls.urls')),
#     url(r'^admin/', include(admin.site.urls)),
# )

urlpatterns = patterns('',
#     (r'^about/', TemplateView.as_view(template_name="about.html")),
#     (r'^/', TemplateView.as_view(template_name="index.html")),
#     url(r'^$', views.index, name='index'),
#    url(r'', include('django.contrib.flatpages.urls')),
#     url(r'about/', include('about')),
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^admin/', include(admin.site.urls)),
    (r'^pages/', include('django.contrib.flatpages.urls')),
)


urlpatterns += patterns('django.contrib.flatpages.views',
    url(r'^/$', 'flatpage', {'url': '/home/'}, name='home'),
    url(r'^home/$', 'flatpage', {'url': '/home/'}, name='home'),
    url(r'^about/$', 'flatpage', {'url': '/about/'}, name='about'),
    url(r'^license/$', 'flatpage', {'url': '/license/'}, name='license'),
)

# urlpatterns += patterns('django.contrib.flatpages.views',
#     (r'^(?P<url>.*/)$', 'flatpage'),
# )

# urlpatterns = patterns('',
#     (r'^pages/', include('django.contrib.flatpages.urls')),
# )
