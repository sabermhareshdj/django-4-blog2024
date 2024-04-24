from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from blog.views import post_list , post_detail,post_new,edit_post,delete_post

urlpatterns = [
    path('admin/' , admin.site.urls),
    path('blog/' , post_list),
    path('blog/new' , post_new),
    path('blog/<int:post_id>' , post_detail),
    path('blog/<int:post_id>/edit' , edit_post),
    path('blog/<int:post_id>/delete' , delete_post),
  

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)