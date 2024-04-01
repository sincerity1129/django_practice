from rest_framework.urlpatterns import format_suffix_patterns
from django.contrib import admin
from django.urls import path
from web_browsable import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("reverse-view/<int:year>/", views.reverse_view, name="reverse"),
    path('format-view/', views.format_view),
]

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'html'])