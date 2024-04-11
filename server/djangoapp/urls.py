# Uncomment the imports before you add the code
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic.base import TemplateView
from . import views

app_name = 'djangoapp'
urlpatterns = [
    # # path for registration
    path('register', views.registration, name='register'),

    # path for login
    path(route='login', view=views.login_user, name='login'),

    # path for logout
    path('logout', views.logout_request, name='logout'),

    # path for get car info
    path('get_cars', views.get_cars, name='getcars'),

    # path for get dealerships
    path('get_dealers', views.get_dealerships, name='get_dealers'),

    # path for get dealerships by state
    path('get_dealers/<str:state>', views.get_dealerships, name='get_dealers_by_state'),

    # path for get dealer by id
    path('dealer/<int:dealer_id>', views.get_dealer_details, name='dealer_details'),

    # path for dealer reviews view
    path('reviews/dealer/<int:dealer_id>', views.get_dealer_reviews, name='dealer_details'),

    # path for add a review view

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
