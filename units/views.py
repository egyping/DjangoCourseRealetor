from django.shortcuts import render, get_object_or_404, redirect
from .models import Unit
from django.urls import reverse
from .forms import UnitForm
from django.views.generic import ListView, DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

def all_units(request):
    ## logic
    all_units = Unit.objects.all()
    return render(request,'units/all_units.html' ,{'units':all_units})


def single_unit(request,slug):
    #logic
    single_unit = Unit.objects.get(slug=slug)
    return render(request,'units/single_unit.html',{'unit':single_unit})


def new_unit(request):
    #print('In View')
    if request.method=='POST':  # new post to the blog
        form = UnitForm(request.POST or None , request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect(reverse('units:all_units_list'))

    else:  # show form 
        form = UnitForm()
    return render(request,'units/new.html',{'form':form})



def unit_edit(request,slug):
    single_unit = Unit.objects.get(slug=slug)
    if request.method=='POST':  # new post to the blog
        form = UnitForm(request.POST or None , request.FILES or None , instance=single_unit)
        if form.is_valid():
            form.save()
            return redirect(reverse('units:all_units_list'))

    else:  # show form 
        form = UnitForm(instance=single_unit)
    return render(request,'units/new.html',{'form':form})


def unit_delete(request, slug):
    obj = get_object_or_404(Unit, slug=slug)
    template_name = 'units/delete.html'
    if request.method == "POST":
        obj.delete()
        return redirect("/units")
    context = {"object": obj}
    return render(request, template_name, context)  



class unit_list(ListView):
    model = Unit



class unit_detail(DetailView):
    model = Unit


class unit_update(UpdateView):
    model = Unit
    fields = ['title','price']
    success_url = '/unit/cbv'