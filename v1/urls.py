from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from v1.views.health import HealthCheck
from v1.views.user import CustomTokenObtainPairView
from v1.views.user.info import UserInfoView
from v1.views.user.create import UserCreateView

from v1.views.taxpayer import TaxPayerAPIView
from v1.views.taxpayer.review_docs import TaxPayerReviewAPIView

urlpatterns = [
    path(
        "health/",
        HealthCheck.as_view(),
    ),
    path("token/", CustomTokenObtainPairView.as_view(), name="token"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("user/", UserInfoView.as_view(), name="user_info"),
    path("user/register/", UserCreateView.as_view(), name="register"),
    path("taxpayer/", TaxPayerAPIView.as_view(), name="taxpayer"),
    path("taxpayer/review/", TaxPayerReviewAPIView.as_view(), name="taxpayer-review"),
]
