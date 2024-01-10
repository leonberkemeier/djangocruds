from django.shortcuts import render
from .models import Cards
from django.contrib import messages
from django.db.models import Q

# Create your views here.

def index(request):
    cards = Cards.objects.all()
    # customers = Card.objects.all()
    query=""

    if request.method == "POST":
        if "add" in request.POST:
            front = request.POST.get("front")
            back = request.POST.get("back")
            Cards.objects.create(
                front=front,
                back=back,

            )
            messages.success(request, "Card has been added Successfully")
        
        elif "edit" in request.POST:
            id = request.POST.get("id")
            front = request.POST.get("front")
            back = request.POST.get("back")

            edit_card = Cards.objects.get(id=id)
            edit_card.front = front
            edit_card.back = back
            edit_card.save()

            messages.warning(request, "Card has been EDDITED")

        elif "delete" in request.POST:
            id = request.POST.get("id")
            card = Cards.objects.get(id=id)

            # print('hi')
            # print(id)
            # print(customer)

            card.delete()

            messages.error(request, "Card has ben DELETED")

        elif "search" in request.POST:
            query = request.POST.get("searchquery")
            customers = Customer.objects.filter(Q(name__icontains=query) | Q (email__icontains=query))



    context = {"cards": cards, "query":query}
    return render(request, "index.html", context=context)