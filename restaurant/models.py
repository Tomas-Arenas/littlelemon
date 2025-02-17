from django.db import models

# Create your models here.
class Booking(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField()
    booking_date = models.DateTimeField()
    
    class Meta:
        db_table = 'booking'
        
    def __str__(self):
        return f"Booking {self.id} - {self.name}"
    
class Menu(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField()
    
    class Meta:
        db_table = 'menu'
        
    def __str__(self):
        return f"Menu {self.id} - {self.name}"