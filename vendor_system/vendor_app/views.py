from django.shortcuts import get_object_or_404
from django.utils import timezone

# Create your views here.


from rest_framework import status,viewsets,generics
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from .models import Vendor
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView

class MyTokenObtainPairView(TokenObtainPairView):
    pass


class VendorViewSet(viewsets.ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    permission_classes = [IsAuthenticated]



class PurchaseOrderViewSet(viewsets.ModelViewSet):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer
    permission_classes = [IsAuthenticated]



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_vendor_performance(request, vendor_id):
    try:
        vendor_performance = HistoricalPerformance.objects.filter(vendor_id=vendor_id).latest('date')
    except HistoricalPerformance.DoesNotExist:
        return Response({"message": "Vendor performance data not found."}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = VendorPerformanceSerializer(vendor_performance)
    return Response(serializer.data)




@api_view(['POST'])
@permission_classes([IsAuthenticated])
def acknowledge_purchase_order(request, po_id):
    purchase_order = get_object_or_404(PurchaseOrder, pk=po_id)
    if purchase_order.acknowledgment_date:
        return Response({"error": "Purchase order is already acknowledged"}, status=status.HTTP_400_BAD_REQUEST)
    purchase_order.acknowledgment_date = timezone.now()
    purchase_order.save(update_fields=['acknowledgment_date'])
    HistoricalPerformance.update_performance_metrics(purchase_order.vendor_id)

    return Response({"message": "Purchase order acknowledged successfully"}, status=status.HTTP_200_OK)