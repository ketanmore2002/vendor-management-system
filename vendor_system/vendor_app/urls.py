from django.urls import path
from .views import *

urlpatterns = [
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/vendors/', vendors_list_create), 
    path('api/vendors/<int:id>/', VendorRetrieveUpdateAPIView.as_view(), name='vendor-detail-update-delete'), 
    path('api/purchase_orders/', purchase_order_list_create),
    path('api/purchase_orders/<int:id>/', PurchaseOrderRetrieveUpdateAPIView.as_view(), name='purchase-order-detail-update-delete'),
    path('api/vendors/<int:vendor_id>/performance/', get_vendor_performance, name='vendor-performance'),
    path('api/purchase_orders/<int:po_id>/acknowledge/', acknowledge_purchase_order, name='acknowledge_purchase_order'),
]
