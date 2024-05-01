from django.db import models
from django.db.models import JSONField 


from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime
from django.db import transaction

# Create your models here.

class Vendor(models.Model):
    name = models.CharField(max_length=100)
    contact_details = models.TextField()
    address = models.TextField()
    vendor_code = models.CharField(max_length=50, unique=True)
    on_time_delivery_rate = models.FloatField(null=True)
    quality_rating_avg = models.FloatField(null=True)
    average_response_time = models.FloatField(null=True)
    fulfillment_rate = models.FloatField(null=True)

    def __str__(self):
        return self.name



class PurchaseOrder(models.Model):
    po_number = models.CharField(max_length=50, unique=True)
    vendor = models.ForeignKey('Vendor', on_delete=models.CASCADE)
    order_date = models.DateTimeField()
    delivery_date = models.DateTimeField()
    items = JSONField()
    quantity = models.IntegerField()
    status = models.CharField(max_length=50)
    quality_rating = models.FloatField(null=True)
    issue_date = models.DateTimeField()
    acknowledgment_date = models.DateTimeField(null=True)

    def __str__(self):
        return self.po_number
    

class HistoricalPerformance(models.Model):
    vendor = models.ForeignKey('Vendor', on_delete=models.CASCADE)
    date = models.DateTimeField()
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()

    # @transaction.atomic
    @classmethod
    def update_performance_metrics(cls, vendor_id):
        completed_pos = PurchaseOrder.objects.filter(vendor_id=vendor_id, status='completed')
        total_completed_pos = completed_pos.count()
        on_time_deliveries = completed_pos.filter(delivery_date__lte=models.F('delivery_date')).count()
        on_time_delivery_rate = (on_time_deliveries / total_completed_pos) * 100 if total_completed_pos > 0 else 0

        quality_rating_avg = completed_pos.aggregate(models.Avg('quality_rating'))['quality_rating__avg'] or 0

        acknowledged_pos = completed_pos.filter(acknowledgment_date__isnull=False)
        response_times = acknowledged_pos.annotate(response_time=models.F('acknowledgment_date') - models.F('issue_date')).aggregate(models.Avg('response_time'))['response_time__avg']
        average_response_time = (response_times.total_seconds() / 3600) if response_times else 0

        total_pos = PurchaseOrder.objects.filter(vendor_id=vendor_id).count()
        fulfilled_pos = PurchaseOrder.objects.filter(vendor_id=vendor_id, status='completed').count()
        fulfillment_rate = (fulfilled_pos / total_pos) * 100 if total_pos > 0 else 0

        cls.objects.create(
            vendor_id=vendor_id,
            date=datetime.now(),
            on_time_delivery_rate=on_time_delivery_rate,
            quality_rating_avg=quality_rating_avg,
            average_response_time=average_response_time,
            fulfillment_rate=fulfillment_rate
        )

@receiver(post_save, sender=PurchaseOrder)
def update_performance_metrics(sender, instance, **kwargs):
    HistoricalPerformance.update_performance_metrics(instance.vendor_id)
