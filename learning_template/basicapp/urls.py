from django.urls import path
from basicapp import views

# template tagging
app_name = 'basicapp'

urlpatterns = [
    path('relative/',views.relative_urls_template,name="relative"),
    path('other/',views.other,name="other")
]
