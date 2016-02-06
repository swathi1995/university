from django.conf.urls import include, url
from register.views import UserRegistrationView
from register.views import UserRegistrationSuccessView
urlpatterns = [
    url(r'^signup/$', UserRegistrationView.as_view(), name='signup'),
    url(r'^user/success/$', UserRegistrationSuccessView.as_view(), name='success_signup'),

    ]