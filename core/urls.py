from django.urls import path
from .views import auth_views
from .views import status_views
from .routes import router

urlpatterns = [
    path('status', status_views.StatusView.as_view()),
    path('register', auth_views.RegisterView.as_view()),
    path('login', auth_views.LoginView.as_view()),
    path('user', auth_views.UserView.as_view()),
    path('logout', auth_views.LogoutView.as_view()),
]

urlpatterns += router.urls