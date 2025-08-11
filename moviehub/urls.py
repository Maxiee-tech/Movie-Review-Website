from django.urls import path, include
from users.views import logout_view
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

def profile_redirect(request):
    if request.user.is_authenticated:
        from users.models import Profile
        profile, created = Profile.objects.get_or_create(user=request.user)
        return redirect('users:profile', pk=profile.pk)
    return redirect('users:login')
"""
URL configuration for moviehub project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('movies/', include('movies.urls')),
    path('reviews/', include('reviews.urls')),
    path('blog/', include('blog.urls')),
    path('users/', include('users.urls')),
    path('login/', RedirectView.as_view(url='/users/login/', permanent=False)),
    path('signup/', RedirectView.as_view(url='/users/register/', permanent=False)),
    path('dashboard/', include('dashboard.urls')),
        path('profile/', profile_redirect, name='profile_redirect'),
    path('logout/', logout_view, name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)