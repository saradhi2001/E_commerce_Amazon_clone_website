from pyexpat.errors import messages
from django.shortcuts import get_object_or_404, render, redirect # type: ignore
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm # type: ignore
from django.contrib.auth import login, logout # type: ignore
from django.db.models import Q # type: ignore
 # type: ignore

from shop.models import Cart, Product

# Homepage View
def index(request):
    products = Product.objects.all()
    return render(request, 'shop/index.html', {'products': products})

# Product Detail View
def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'shop/product_detail.html', {'product': product})

# Cart View
def cart(request):
    cart_items = Cart.objects.all()
    return render(request, 'shop/cart.html', {'cart_items': cart_items})

# Checkout View
def checkout(request):
    return render(request, 'shop/checkout.html')

# Login View
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
    else:
        form = AuthenticationForm()
    return render(request, 'shop/login.html', {'form': form})

# Sign Up View

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # This saves the user to the database
            messages.success(request, 'Your account has been created successfully! You can now log in.')
            return redirect('/')
        else:
            messages.error(request, 'There was an error creating your account. Please try again.')
    else:
        form = UserCreationForm()

    return render(request, 'shop/signup.html', {'form': form})


# Logout View
def logout_view(request):
    logout(request)
    return redirect('/')



# Search View
def search_view(request):
    query = request.GET.get('query', '')
    if query:
        products = Product.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )
    else:
        products = Product.objects.none()
    return render(request, 'shop/search_results.html', {'products': products, 'query': query})


from django.shortcuts import render # type: ignore
from .models import Product  # Replace with your actual model

def search_results(request):
    query = request.GET.get('q', '')
    results = Product.objects.filter(name__icontains=query)  # Adjust based on your search logic
    return render(request, 'shop/search_results.html', {'results': results})


