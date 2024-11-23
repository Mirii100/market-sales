from django.shortcuts import render,get_object_or_404,redirect
from.models import Item,Category
from django.contrib.auth.decorators import login_required
from .forms import NewItemForm,EditItemForm
from django.db.models import Q
# Create your views here.
def browse(request):
    categories=Category.objects.all()
    category_id=request.GET.get('category_id',0)
    query=request.GET.get('query','')
    items=Item.objects.filter(is_sold=False)


    if category_id:
        items=items.filter(category_id=category_id)

    if query:
        items=items.filter(Q(name__icontains=query)|Q(description__icontains=query))

    return render(request,'items.html',{'items':items,'query':query,'categories':categories,'category_id':int(category_id)})



def item_detail(request,pk):
    item=get_object_or_404(Item,pk=pk)
    related_items=Item.objects.filter(category=item.category,is_sold=False).exclude(pk=pk)

    return render(request,"details.html",{'item':item,'related':related_items})

@login_required
def new(request):
    if request.method =='POST':
        form=NewItemForm(request.POST,request.FILES)

        if form.is_valid:
            item=form.save(commit=False)
            item.created_by=request.user
            item.save()


            return redirect('items:detail',pk=item.id)
        
    else:
        form=NewItemForm()

    return render(request,'form.html',{'form':form,'title':'new item'})


@login_required
def delete(request,pk):
    item=get_object_or_404(Item,pk=pk,created_by=request.user)
    item.delete()
    

    return redirect('dashboard:index')


@login_required
def edit(request,pk):
    item=get_object_or_404(Item,pk=pk,created_by=request.user)
    if request.method =='POST':
        form=EditItemForm(request.POST,request.FILES,instance=item)

        if form.is_valid:
            form.save()


            return redirect('items:detail',pk=item.id)
        
    else:
        form=EditItemForm(instance=item)

    return render(request,'form.html',{'form':form,'title':'edit item'})


