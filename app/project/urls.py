from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views

from apps.core.views import frontpage, signup, plans

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', frontpage, name='frontpage'),
    path('plans/', plans, name='plans'),
    path('signup/', signup, name='signup'),
    path('login/', views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),

    path('app/', include('apps.dashboard.urls')),
]
