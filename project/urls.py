from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from blog.views import  PostList , PostDetail,PostCreate,PostUpdate,PostDelete

urlpatterns = [
    path('admin/' , admin.site.urls),
    path('blog/' , PostList.as_view()),
    path('blog/new' , PostCreate.as_view()),
    path('blog/<int:pk>' , PostDetail.as_view()),
    path('blog/<int:pk>/edit' , PostUpdate.as_view()),
    path('blog/<int:pk>/delete' , PostDelete.as_view()),
  

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)