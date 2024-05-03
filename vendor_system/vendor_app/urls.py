from django.urls import path
from .views import MyTokenObtainPairView,get_vendor_performance,acknowledge_purchase_order


urlpatterns = [
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/vendors/<int:vendor_id>/performance/', get_vendor_performance, name='vendor-performance'),
    path('api/purchase_orders/<int:po_id>/acknowledge/', acknowledge_purchase_order, name='acknowledge_purchase_order'),
]
