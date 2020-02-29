from django.contrib import admin
from django.conf import settings # new
from django.urls import path, include # new
from django.conf.urls.static import static # new
from django.conf.urls import url

from details import views
from ratings import views as ratings_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name ='home'),
    url(r'^details/(\d+)/', views.book_detail, name='book_detail'),
    url(r'^reviews/(\d+)/', ratings_views.display_comment, name='display_comment'),
    url(r'^details/review/(\d+)/', ratings_views.write_comment, name='write_comment'),
    url(r'^details/rate/(\d+)/', ratings_views.rate_book, name='rate_book'),
]

if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
