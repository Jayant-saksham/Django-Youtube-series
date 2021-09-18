
from django.urls import path
from account.views.loginmethod import LoginMethod
from account.views.signup import SignupMethod
from account.views.LogoutMethod import LogoutMethod

urlpatterns = [
    path('login/', LoginMethod.as_view(), name="login_page"),
    path('signup/', SignupMethod.as_view(), name="signup_page"),
    path('logout/', LogoutMethod.as_view(), name = "logout_page")
]
