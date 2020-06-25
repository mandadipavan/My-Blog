from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import ModelData
from .forms import TodoForm


# Create your views here.
def TodoView(request):
	items = ModelData.objects.all()
	form=TodoForm()
	if request.method == 'POST':
		form = TodoForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('/') 	
	return render(request,'todo/list.html',{'all_items':items, 'form':form})


def UpdateList(request, pk):
	item=ModelData.objects.get(id=pk)
	formx=TodoForm(instance=item)
	if request.method=='POST':
		formy=TodoForm(request.POST, instance=item)
		if formy.is_valid():
			formy.save()
			return redirect('/')

	return render(request, 'todo/update_list.html',{'form':formx})


def DeleteList(request, pk):
	item=ModelData.objects.get(id=pk)
	if request.method=='POST':
		item.delete()
		return redirect('/')
	return render(request, 'todo/delete.html')