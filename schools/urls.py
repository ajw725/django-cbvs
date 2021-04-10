from django.urls import path
from schools import views

app_name = 'schools'

urlpatterns = [
    path('', views.SchoolListView.as_view(), name='list'),
    path('<int:pk>', views.SchoolDetailView.as_view(), name='detail'),
    path('new', views.SchoolCreateView.as_view(), name='new'),
    path('<int:pk>/edit', views.SchoolUpdateView.as_view(), name='edit'),
    path('<int:pk>/delete', views.SchoolDeleteView.as_view(), name='delete')
]
