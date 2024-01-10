from django.shortcuts import render
from .models import Customer
from django.contrib import messages
from django.db.models import Q

# Create your views here.

def index(request):
    customers = Customer.objects.all()
    query=""

    if request.method == "POST":
        if "add" in request.POST:
            name = request.POST.get("name")
            email = request.POST.get("email")
            Customer.objects.create(
                name=name,
                email=email,

            )
            messages.success(request, "Customer has been ADDED successfully")
        
        elif "edit" in request.POST:
            id = request.POST.get("id")
            name = request.POST.get("name")
            email = request.POST.get("email")

            edit_customer = Customer.objects.get(id=id)
            edit_customer.name = name
            edit_customer.email = email
            edit_customer.save()

            messages.warning(request, "Customer has been EDDITED")

        elif "delete" in request.POST:
            id = request.POST.get("id")
            customer = Customer.objects.get(id=id)

            print('hi')
            print(id)
            print(customer)

            customer.delete()

            messages.error(request, "Customer has ben DELETED")

        elif "search" in request.POST:
            query = request.POST.get("searchquery")
            customers = Customer.objects.filter(Q(name__icontains=query) | Q (email__icontains=query))



    context = {"customers": customers, "query":query}
    return render(request, "index.html", context=context)