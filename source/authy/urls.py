from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from authy.views import EditProfile, CustomLogoutView

urlpatterns = [
    path('profile/edit', EditProfile, name="editprofile"),
    path('sign-up/', views.register, name="sign-up"),
    path('sign-in/', auth_views.LoginView.as_view(template_name="sign-in.html", redirect_authenticated_user=True), name='sign-in'),
    path('sign-out/', CustomLogoutView.as_view(), name='sign-out'),
]
