from django.contrib import admin
from django.urls import path
from cloneamazonapp import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('demo',views.demoPage),
    path('demoPage',views.demoPageTemplate),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

