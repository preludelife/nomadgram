from django.conf.urls import url

from . import views

app_name = "users"
urlpatterns = [
    # path("", view=views.UserListView.as_view(), name="list"),
    # path("~redirect/", view=views.UserRedirectView.as_view(), name="redirect"),
    # path("~update/", view=views.UserUpdateView.as_view(), name="update"),
    # path(
    #     "<str:username>",
    #     view=views.UserDetailView.as_view(),
    #     name="detail",
    # ),
    url(
        regex=r'^explore$',
        view=views.ExploreUsers.as_view(),
        name='explore_users'
    ),
    url(
        regex=r'(?P<user_id>[0-9]+)/follow/$',
        view=views.FollowUser.as_view(),
        name='follow_user'
    ),
    url(
        regex=r'(?P<user_id>[0-9]+)/unfollow/$',
        view=views.UnFollowUser.as_view(),
        name='follow_user'
    ),
    url(
        regex=r'^(?P<username>\w+)/$',
        view=views.UserProfile.as_view(),
        name='user_profile'
    ),
]
