from django.urls import path 
from .views import PostList, PostDetail

app_name = 'blog_api'

urlpatterns = [
    ##two endpoints showing detail post and list of views
    ##views will take in primary key
    ##second view to show all data in database
    ##one view will show one post in database
    path('<int:pk>/', PostDetail.as_view(), name='detailcreate'),
    path('', PostList.as_view(), name='listcreate')
]