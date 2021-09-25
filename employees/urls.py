from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('delete/<str:id>/',views.delete,name='delete'),
    path('update/<str:id>/',views.update,name='update'),
]

from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)





