from django.shortcuts import render,get_object_or_404,redirect
from.models import Conversation
from items.models import Item
from .forms import conversationMessageForm
# Create your views here.

def new_conversation(request,item_pk):
    item=get_object_or_404(Item,pk=item_pk)

    if item.created_by==request.user:
        return redirect('dashboard:index')
    conversation=Conversation.objects.filter(item=item).filter(members__in=[request.user.id])

    if conversation:
        pass

    if request.method=='POST':
        form=conversationMessageForm(request.POST)
        if form.is_valid():
            conversation=Conversation.objects.create(item=item)
            conversation.members.add(request.user)
            conversation.members.add(item.created_by)
            conversation.save()


            conversation_message=form.save(commit=False)
            conversation_message.conversation=conversation
            conversation_message.created_by=request.user
            conversation_message.save()
            #erdirecting
            return redirect('items:detail',pk=item_pk)
        
    else:
        form=conversationMessageForm()

    return render(request,'new.html',{'form':form})

        



