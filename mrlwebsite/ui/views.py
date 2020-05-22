from django.shortcuts import render
from .models import Master,Countries,ComCountryRelation,RegulatoryParameters,TypeOfParameters,Profile,Commodities
# Create your views here.
from django.http import HttpResponse
from django.db.models import Q
from django.shortcuts import redirect
import xlwt
import csv
from operator import itemgetter
from itertools import groupby

from .forms import Getdata
def index(request):
    countrieslist=request.session['col']
    commoditylist=request.session['coml']
    parameterlist=request.session['parl']
    master=Master.objects.filter(Q(country__in=countrieslist)&Q(product__in=commoditylist)&Q(parameter__in=parameterlist)).all()
    

    
    # master_by_countries=Master.objects.values('country')
    # master_by_commodities=Master.objects.values('product')
    # master_by_country_commodity=master.filter()
    # master_by_parameters=Master.objects.values('parameter')
    # for country in master_by_countries:
    #     for commodity in master_by_commodities:
    #         for parameter in master_by_parameters:
    #             master.filter()
    countries=Countries.objects.all()
    com=Commodities.objects.all()
    comcon=ComCountryRelation.objects.all()
    params=RegulatoryParameters.objects.all()
    paramtype=TypeOfParameters.objects.all()
    prof=Profile.objects.all()
    
    
    return render(request,'report.html',{'master': master,'countries':countries,'com':com,'comcon':comcon,'params':params,'paramtype':paramtype,'prof':prof})


# def new_report(request):
#     form=Getdata(request.POST or None)
#     if request.POST:
#         data=request.POST.copy()
#         countrylist=data.getlist('countries')
#         comlist=data.getlist('commodities')
#         paramlist=data.getlist('parameters')



def form(request):
    # context={'form':}
    form=Getdata(request.POST or None)
    # context['form']= Getdata()
    if request.POST:
        # if form.is_valid():
            data = request.POST.copy()
            request.session['col']=data.getlist('countries')
            request.session['coml']=data.getlist('commodities')
            request.session['parl']=data.getlist('parameters')
            return redirect('/ui')
            # temp=form.cleaned_data.get()
            # print(temp)
    return render(request,"form.html",{'form':form,})

def excel_view(request):
    normal_style = xlwt.easyxf("""
     font:
         name Verdana
     """) 
    response = HttpResponse(content_type='ui/ms-excel')
#     response['Content-Disposition'] = 'attachment; filename="data.csv"'
#     writer = csv.writer(response)
#     writer.writerow(['Username', 'First name', 'Last name', 'Email address'])

    # print(request.GET.copy())
    wb = xlwt.Workbook()
    ws0 = wb.add_sheet('Worksheet')
    ws0.write(0, 0, "something", normal_style)
    wb.save(response)
    return response

