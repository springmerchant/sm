from django.conf.urls.defaults import *
from sm.subscribe.views import SubscribeView, SuccessView

urlpatterns = patterns('',
    url(r'^$', SubscribeView.as_view(), name='subscribe_view'),
    url(r'^success/$', SuccessView.as_view(), name='subscribe_success'),

)
