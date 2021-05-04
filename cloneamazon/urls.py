from django.contrib import admin
from django.urls import path
from cloneamazonapp import views,AdminViews
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', views.adminLogin),
    path('demo',views.demoPage),
    path('demoPage',views.demoPageTemplate),
    path('admin_login_process',views.adminLoginProcess, name = "admin_login_process" ), 

    # PAGE FOR ADMIN
    path('admin_home',AdminViews.admin_home)

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

