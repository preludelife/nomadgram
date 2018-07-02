from django.conf.urls import url
from . import views

app_name = "images"
urlpatterns = [
    url(
        regex=r'^all/$',
        view=views.Feed.as_view(),
        name='feed'
    ),
    url(
        regex=r'^(?P<image_id>\w+)/like/$',
        view=views.LikeImage.as_view(),
        name='like_image'
    ),
    url(
        regex=r'^(?P<image_id>\w+)/unlike/$',
        view=views.UnLikeImage.as_view(),
        name='like_image'
    ),
    url(
        regex=r'^(?P<image_id>\w+)/comments/$',
        view=views.CommentOnImage.as_view(),
        name='comment_image'
    ),
    url(
        regex=r'^comments/(?P<comment_id>[0-9]+)/$',
        view=views.Comment.as_view(),
        name='comment'
    ),
    url(
        regex=r'^search/$',
        view=views.Search.as_view(),
        name='search'
    )

    # /images/3/like
    # 0 create the url and the view
    # 1 take the id from the url
    # 2 we want to find an image with this id
    # 3 we want to create a like for that image

    # url(
    #     regex=r'^all/$',
    #     view=views.ListAllImages.as_view(),
    #     name='all_images'
    # ),
    # url(
    #     regex=r'^comments/$',
    #     view=views.ListAllComments.as_view(),
    #     name='all_images'
    # ),
    # url(
    #     regex=r'^likes/$',
    #     view=views.ListAllLikes.as_view(),
    #     name='all_images'
    # ),



]
