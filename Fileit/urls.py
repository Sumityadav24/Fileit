
from django.contrib import admin
from django.urls import path
from myapp import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/',views.HandleSignUp,name="signup"),
    path('login/',views.HandleLogin,name="login"),
    path('logout/',views.HandleLogout,name="logout"),
    path('upload/',views.HandleUpload,name="upload")
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
