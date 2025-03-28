from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'recipes'

urlpatterns = [
    path('', views.home, name="home"),
    path('recipes/category/<int:category_id>/',
        views.category, name="category"),
    path('recipes/<int:id>/', views.recipe, name="recipe"),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)