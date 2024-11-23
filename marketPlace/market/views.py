from django.shortcuts import render,redirect
from items.models import Item,Category
from .forms import SignupForm
# Create your views here.
def home(request):
    items=Item.objects.filter(is_sold=False)
    categories=Category.objects.all()
    return render(request,"home.html",{'item':items,'categories':categories})

def contact(request):
    return render(request,"contact.html")

def signup(request):
    if request.method=='POST':
        form=SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:

        form=SignupForm()

    return render(request,'signup.html',{'form':form})

