from django.shortcuts import render
from .models import Customer
from django.contrib import messages
from django.db.models import Q
import random

# Create your views here.

def index(request):
    customers = Customer.objects.all()
    questioncustomer = Customer.objects.order_by("id").first()
    # firstcustomer = Customer.objects.order_by("id").first()
    # lastcustomer = Customer.objects.order_by("id").last()
    
    # # fc = Customer.objects.get(id=id).pk
    # countcustomers = Customer.objects.count()
    # a = 0
    # b = countcustomers-1
    
    # rnd = random.randint(a, b)
    
    # rndcustomer = Customer.objects.order_by("id").all()[rnd:rnd+1]

    # fc = rndcustomer[0]


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

            customer.delete()

            messages.error(request, "Customer has ben DELETED")

        elif "search" in request.POST:
            query = request.POST.get("searchquery")
            customers = Customer.objects.filter(Q(name__icontains=query) | Q (email__icontains=query))





    context = {
            "customers": customers, 
            "query":query,
            "questioncustomer":questioncustomer,
            # "firstcustomer":firstcustomer,
            # "lastcustomer":lastcustomer,
            # "rnd": rnd,
            # "rndcustomer": rndcustomer,
            # "coutcustomer":countcustomers,
            # "fc": fc,
               }
    return render(request, "index.html", context=context)



def renderrndtpl(request):
    questioncustomer = randomCustomer()
    # nc = nextCustomer()
    context = {
        "questioncustomer":questioncustomer,
        # "nc":nc,
    }
    return render(request, 'modal.html',context=context)

def randomCustomer():
    
    countcustomers = Customer.objects.count()
    a = 0
    b = countcustomers-1
    
    rnd = random.randint(a, b)
    
    rndcustomer = Customer.objects.order_by("id").all()[rnd:rnd+1]

    fc = rndcustomer[0]

    return fc

def rendernexttpl(request):
    questioncustomer = nextCustomer(request)
    context={
        'questioncustomer': questioncustomer,
    }
    print(context)
    return render(request, 'modal.html',context=context)

def nextCustomer(request):
    # customers=Customer.objects.all()
    # allcustomers = Customer.objects.all()
    # # questioncustomer=None
    # try:

    #     after=request.GET.get('after', None)
    #     # not NONE
    #     if after is not None:
    #         questioncustomer=Customer.objects.filter(id__gt=after).order_by('id')[0]
    #         print('After is not NONE')
    #     # IS NONE
    #     else:
    #         questioncustomer=Customer.objects.order_by('id')[0]
    #         print("After is NONE")
    
    # except IndexError:
    #     if len(allcustomers) > 0:
    #         questioncustomer=allcustomers[0]
    # except ValueError:
    #     if len(allcustomers) > 0:
    #         questioncustomer=allcustomers[0]
    

    # nc = questioncustomer
    # context ={
    #     'questioncustomer':questioncustomer,
    #     'allcustomers':allcustomers,
    # # }




    allcustomers = Customer.objects.all()

    try:
         
        after=request.GET.get('after', None)
        before=request.GET.get('before', None)
        both=after and before
        if after is not None:
            print('notnone')
            questioncustomer=allcustomers.filter(id__gt=after).order_by('id')[0]
        elif before is not None:
            print('notnone')
            questioncustomer=allcustomers.filter(id__lt=before).order_by('-id')[0]
        # elif both:
        #     questioncard=Card.ozbjects.filter(id__gt=after).order_by('id')[0]
        else:
            print("stillnone")
            questioncustomer=allcustomers.order_by('id')[0]
    
    except IndexError:
        if len(allcustomers) > 0:
            questioncustomer=allcustomers[0]
    except ValueError:
        if len(allcustomers) > 0:
            questioncustomer=allcustomers[0]
        
    return questioncustomer

# def renderprevtpl(request):
#     pc = nextCustomer()

#     context={
#         'pc':pc,
#     }
#     return render(request, 'modal.html',context=context)


def test(request):
    return render(request, "test.html")