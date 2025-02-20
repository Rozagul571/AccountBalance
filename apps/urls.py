from allauth.account.views import LogoutView
from django.conf.urls.static import static
from django.urls import path, include
from apps.views import home_view, expenses, login_form_view, register_form_view, income, logout_view
from root.settings import MEDIA_URL, MEDIA_ROOT

urlpatterns = [
    path('', home_view, name='home'),
    path('login/', login_form_view, name='login'),
    path('register/', register_form_view, name='register'),
    path('income/', income, name='income'),
    path('expenses/', expenses, name='expenses'),
    path('logout', logout_view, name='logout'),

    # path('accounts/', include('allauth.urls')),

    # path('accounts/password/reset/', include('django.contrib.auth.urls')),
] + static(MEDIA_URL, document_root=MEDIA_ROOT)
