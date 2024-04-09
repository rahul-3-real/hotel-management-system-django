from django.db import models
from django.contrib.auth.models import AbstractUser


# Accounts Model
class Account(AbstractUser):
    USER_TYPE_CHOICES = (
        ("admin", "Admin"),
        ("staff", "Staff"),
        ("guest", "Guest"),
    )
    GENDER_CHOICES = (
        ("male", "Male"),
        ("female", "Female"),
        ("other", "Other"),
    )

    type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default="guest")
    name = models.CharField(max_length=255)
    dob = models.DateField(null=True, blank=True, verbose_name="Date of Birth")
    gender = models.CharField(
        max_length=10, choices=GENDER_CHOICES, null=True, blank=True
    )
    phone = models.CharField(
        max_length=15, null=True, blank=True, verbose_name="Phone Number"
    )
    phone_alt = models.CharField(
        max_length=15, null=True, blank=True, verbose_name="Alternate Phone Number"
    )
    email_alt = models.EmailField(
        null=True, blank=True, verbose_name="Alternate Email Address"
    )
    address = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username


# Admin Model
class Admin(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


# Staff Model
class Staff(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


# Guest Model
class Guest(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


# Job Position Model
class JobPosition(models.Model):
    position = models.CharField(max_length=255, unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.position


# Salary Model
class Salary(models.Model):
    staff = models.ForeignKey(Staff, null=True, blank=True, on_delete=models.SET_NULL)
    job_position = models.ForeignKey(
        JobPosition, null=True, blank=True, on_delete=models.SET_NULL
    )
    base_salary = models.CharField(max_length=255)
    deduction = models.CharField(max_length=255)
    total_salary = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.staff} - {self.job_position}"
