from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = "accounts"

urlpatterns = [
    path("register/", views.register_view, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
]

# Does not work

# path(
#     "password-reset/",
#     auth_views.PasswordResetView.as_view(
#         template_name="accounts/password-reset.html",
#     ),
#     name="password-reset",
# ),
# path(
#     "password-reset-done/",
#     auth_views.PasswordResetDoneView.as_view(
#         template_name="accounts/password-reset-done.html",
#     ),
#     name="password-reset-done",
# ),
# path(
#     "password-reset-confirm/<uidb64>/<token>/",
#     auth_views.PasswordResetConfirmView.as_view(
#         template_name="accounts/password-reset-confirm.html",
#     ),
#     name="password-reset-confirm",
# ),
# path(
#     "password-reset-complete/",
#     auth_views.PasswordResetCompleteView.as_view(
#         template_name="accounts/password-reset-complete.html",
#     ),
#     name="password-reset-complete",
# ),
