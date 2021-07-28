import debug_toolbar
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.views.static import serve as mediaserve
from django.conf.urls import url
from . import settings
from main.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('captcha/', include('captcha.urls')),
    path('', include('main.urls')),
]

if settings.DEBUG:
    urlpatterns = [path('__debug__/', include(debug_toolbar.urls)), ] + urlpatterns
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += [url(f'^{settings.MEDIA_URL.lstrip("/")}(?P<path>.*)$',
                        mediaserve, {'document_root': settings.MEDIA_ROOT}),
                    url(f'^{settings.STATIC_URL.lstrip("/")}(?P<path>.*)$',
                        mediaserve, {'document_root': settings.STATIC_ROOT}),
                    ]


handler404 = page_not_found
