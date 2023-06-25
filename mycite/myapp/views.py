from django.shortcuts import render
from django.views.generic import View,ListView
from django.views.generic.edit import UpdateView,DeleteView,CreateView
from .models import *

# Create your views here.

class Index(View):
    def get(self,request):
        people = Member.objects.all()
        context = {
            'people' : people
        }
        return render(request, 'index.html',context )
    
class ListCreateview(CreateView):
    model = Member
    fields = '__all__'
    template_name = 'create.html'
    success_url = '/'
    
class Updateview(UpdateView):
    model = Member
    fields = ['name', 'surname','pay']
    template_name = 'create.html'
    success_url = '/'

class DeleteStudentView(DeleteView):
	model = Member
	fields = ['name', 'surname','pay']
	template_name = 'delete.html'
	success_url = '/'
    
class PayListview(ListView):
     def get(self,request):
        tolaganlar = Member.objects.filter(pay=True)
        context={
             'tolaganlar' : tolaganlar
        }
        return render(request,'pay/pay.html', context)
     
class PaidListview(ListView):
     def get(self,request):
        tolamaganlar = Member.objects.filter(pay=False)
        context={
             'tolamaganlar' : tolamaganlar
        }   
        return render(request,'pay/unpaid.html', context)
        
def search_base(request):
	q = request.GET.get('searchis', None)
	people = Member.objects.filter(title__icontains=q)
	query = request.GET['searchis']
	context = {
		'people': people,
        'query' : query
	}
	return render(request, 'searcheresult.html', context)