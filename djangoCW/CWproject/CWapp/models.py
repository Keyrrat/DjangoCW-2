# KIRAT ASLAM

from django.db import models

# Create your models here.

class Devices(models.Model):
    DEVICE_TYPES = [
        ('PC/Laptop', 'PC/Laptop'),
        ('VR Headset', 'VR Headset'),
        ('Camera/Sensors', 'Camera/Sensors'),
        ('PC Peripherals', 'PC Peripherals'),
        ('Furniture', 'Furniture'),
        ('Tripod', 'Tripod'),
        ('VR Controller', 'VR Controller'),
        ('Phones/Tablets', 'Phones/Tablets'),
        ('Other', 'Other'),
    ]

    LOCATIONS = [
        ('XRLab Blue Cabinet', 'XRLab Blue Cabinet'),
        ('XRLab', 'XRLab'),
        ('XRLab Blue Cabinet Large', 'XRLab Blue Cabinet Large'),
        ('XRLab Medium Wooden Cabinet', 'XRLab Medium Wooden Cabinet'),
        ('Other', 'Other'),
    ]

    EQUIPMENT_STATUS = [
        ('On_loan', 'On loan'),
        ('Repairing', 'Repairing'),
        ('Available', 'Available'),
        ('Decommissioned', 'Decommissioned'),
    ]

    equipmentID = models.AutoField(primary_key=True)
    deviceName = models.CharField(max_length=75, unique=True, verbose_name="Device Name")
    device_Type = models.CharField(max_length=75, choices=DEVICE_TYPES, default='Other', verbose_name="Device Type")
    quantity = models.PositiveSmallIntegerField(default=1)
    audit = models.DateField(auto_now_add=True, verbose_name="Audit")
    location = models.CharField(max_length=75, choices=LOCATIONS, default='XRLab', verbose_name="Location")
    comments = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=75, choices=EQUIPMENT_STATUS, default='Available', verbose_name="Status")

    def __str__(self):
        return self.deviceName
    
  
