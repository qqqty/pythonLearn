from django.conf.urls import patterns, include, url
from django.contrib import admin

from study import views as study_views
from account import views as account_views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Tee.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^index/', study_views.index),
    url(r'^show/', study_views.show),
    url(r'^add/', study_views.add),
    url(r'^sum/(\d+)/(\d+)/', study_views.sum, name='sum'),
    url(r'^tpl/', study_views.tpl),
    url(r'^page/(\d+)/', study_views.page),

    url(r'^test/', account_views.test),
    url(r'^login/', account_views.login),
    url(r'^reg/', account_views.reg),
    url(r'^account/', account_views.account),
    url(r'^logout/', account_views.logout),

    url(r'^addVote/', account_views.addVote),
    url(r'^vote/(\d+)/', account_views.vote),
)
