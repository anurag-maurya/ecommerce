from django.urls import path
# # from rest_framework_simplejwt.views import (
# #     TokenObtainPairView,
# #     TokenRefreshView,
# # )
# from .views import user_register
# from rest_framework.authtoken.views import obtain_auth_token
from .views import add_and_get_cart
urlpatterns = [
    # path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path("register/", user_register, name="register"),
    # path("login/", obtain_auth_token),
    path("cart/",add_and_get_cart)
    
]




