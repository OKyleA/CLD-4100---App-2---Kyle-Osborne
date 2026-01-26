from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Product


# View to display all products in the inventory
@login_required
def all_products(request):
    # Fetch every product from the database
    products = Product.objects.all()
    # Pass the list to the template for display
    return render(request, 'all_products.html', {'products': products})


# View for searching products by their unique ProductNumber
@login_required
def search_product(request):
    # Only handle GET requests (form submission)
    if request.method == 'GET':
        # Get the search term from the URL query string (?product_number=...)
        product_number = request.GET.get('product_number')

        if product_number:
            # Filter products where ProductNumber exactly matches (case-sensitive)
            # Note: your model field is ProductNumber, not product_number
            products = Product.objects.filter(ProductNumber=product_number)
            # Show results page with matching products
            return render(request, 'search_results.html', {
                'products': products,
                'product_number': product_number  # Pass back what was searched for display
            })

    # If no search term (or first visit), show the empty search form
    return render(request, 'search_form.html')