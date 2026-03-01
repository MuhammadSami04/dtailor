from django.db import models


# 1️⃣ Customer Model
class Customer(models.Model):
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )

    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)

    def __str__(self):
        return self.name


# 2️⃣ Measurement Model
class Measurement(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    
    chest = models.FloatField()
    waist = models.FloatField()
    shoulder = models.FloatField()
    arm_length = models.FloatField()
    shalwar_length = models.FloatField()
    collar = models.FloatField()

    date_taken = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Measurement - {self.customer.name}"


# 3️⃣ Order Model
class Order(models.Model):
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Ready', 'Ready'),
        ('Delivered', 'Delivered'),
    )

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    dress_type = models.CharField(max_length=100)
    fabric_provided = models.BooleanField(default=True)

    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    advance_payment = models.DecimalField(max_digits=10, decimal_places=2)

    order_date = models.DateField(auto_now_add=True)
    delivery_date = models.DateField()

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')

    def remaining_payment(self):
        return self.total_price - self.advance_payment

    def __str__(self):
        return f"Order #{self.id} - {self.customer.name}"


# 4️⃣ Payment Model
class Payment(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Payment for Order #{self.order.id}"