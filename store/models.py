from django.db import models

# Model for store departments
class Department(models.Model):
    # Unique ID for the department (e.g., 1 for Snacks)
    DepartmentNumber = models.IntegerField(primary_key=True)
    # Name of the department (e.g., Beverages, Candy)
    DepartmentName = models.CharField(max_length=100)

    # How this object appears in admin and dropdowns
    def __str__(self):
        return self.DepartmentName

    # Admin display settings
    class Meta:
        verbose_name = "Department"
        verbose_name_plural = "Departments"
        ordering = ['DepartmentNumber']


# Model for individual products in inventory
class Product(models.Model):
    # Auto-generated unique ID (Django handles this)
    ProductID = models.AutoField(primary_key=True)
    # Product name (e.g., Coca-Cola 12oz)
    ProductName = models.CharField(max_length=100)
    # Unique product code/SKU (e.g., CCOLA-001)
    ProductNumber = models.CharField(max_length=50, unique=True)
    # Date added or manufactured
    ProductDate = models.DateField()
    # Link to the department this product belongs to
    # CASCADE = delete products if their department is deleted
    DepartmentNumber = models.ForeignKey(Department, on_delete=models.CASCADE)

    # How this object appears in admin and lists
    def __str__(self):
        return f"{self.ProductName} ({self.ProductNumber})"

    # Admin display settings
    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        ordering = ['ProductName']