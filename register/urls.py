from django.conf.urls import include, url
from register.views import UserRegistrationView
from register.views import UserRegistrationSuccessView
from register.views import UserDashboardView
urlpatterns = [
    url(r'^signup/$', UserRegistrationView.as_view(), name='signup'),
    url(r'^user/success/$', UserRegistrationSuccessView.as_view(), name='success_signup'),
     url(r'^dash/$', UserDashboardView.as_view(), name='dash'),


    ]