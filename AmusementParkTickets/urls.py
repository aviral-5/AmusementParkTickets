"""AmusementParkTickets URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path,include
from AmusementParkTickets import settings
from django.conf.urls.static import static
from rest_framework.documentation import include_docs_urls


urlpatterns = [
    path('jet/', include('jet.urls', 'jet')),
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    path('accounts/', include('rest_framework.urls')),
    path('apidocs/', include_docs_urls(title='Amusement Park Tickets APIs Doc')),
    path('', admin.site.urls),
    path('api/Authentication/', include('AuthApis.urls')),
    path('api/UserMgmt/', include('UserManagement.urls')),
    path('api/Ticket/', include('Tickets.urls')),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)



