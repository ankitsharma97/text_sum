# from django.urls import path
# from .views import UserCreateView, UserListView, SummarizeTextView, SummarizationStatusView

# urlpatterns = [
#     path('register/', UserCreateView.as_view(), name='register'),
#     path('users/', UserListView.as_view(), name='users'),
#     path('summarize/', SummarizeTextView.as_view(), name='summarize'),
#     path('summarization_status/<str:job_id>/', SummarizationStatusView.as_view(), name='summarization_status'),
# ]


from django.urls import path
from .views import RegisterUser, LoginUser, LogoutUser, UserDetail, FindUsers, SummarizeText

urlpatterns = [
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', LogoutUser.as_view(), name='logout'),
    path('user/<int:pk>/', UserDetail.as_view(), name='user-detail'),
    path('users/', FindUsers.as_view(), name='find-users'),
    path('summarize/', SummarizeText.as_view(), name='summarize-text'),
]
