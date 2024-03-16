from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.conf import settings
from .models import table
from .models import jew
from .models import staf
from .models import ad
from .models import cus
from .models import order
from .models import cart
from .forms import AddForm
from .forms import up
from .forms import im
from django.core.mail import send_mail

from django.contrib.auth import logout

#staff login
def login(request):
    return render(request,'login.html')
#staff login
def loguser(request):
    if request.method== 'POST':
      email = request.POST.get('email')
      password = request.POST.get('password')
      cr = staf.objects.filter(email=email, password=password)
      if cr:
        user_details=staf.objects.get(email=email,password=password)
        id=user_details.id
        name=user_details.name
        request.session['id']=id
        request.session['name']=name

    
        return redirect('wel')

      else:
        return render(request,'login.html')
    else:
        return render(request,'reg.html')



def wel (request):
  id = request.session['id']
  name = request.session['name']

  return render (request,'wel.html',{'id':id,'name':name})

  


def reg(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        table(name=name,email=email,password=password).save()
    return render (request,"reg.html")

def index(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        enq(name=name,email=email,message=message).save()
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def ser(request):
    return render(request,'ser.html')

def adm(request):
    return render(request,'admin.html')

def aduser(request):
  if request.method== 'POST':
      email = request.POST.get('email')
      password = request.POST.get('password')
      cr = ad.objects.filter(email=email, password=password)
      if cr:
        user_details=ad.objects.get(email=email,password=password)
        id=user_details.id
        
        request.session['id']=id
        

    
        return redirect('admm')

      else:
        return render(request,'admin.html')
  else:
        return render(request,'reg.html')

   


def view(request):
  cr = table.objects.all()
  return render(request,'view.html',{'cr':cr})

def add(request,pk):
  cr=table.objects.get(id=pk)
  form=AddForm(instance=cr)
  if request.method=="POST":
    form=AddForm(request.POST,instance=cr)
    if form.is_valid:
        
      name = request.POST.get('name')
      email = request.POST.get('email')
      password = request.POST.get('password')

      staf(name=name,email=email,password=password).save()
      cr.delete()
    redirect('view')
  return render(request,"add.html",{'form':form})

def delete(request,pk):
   cr = table.objects.get(id =pk)
   cr.delete()
   return redirect("view")

def admm(request):
    id = request.session['id']
    return render(request,'admm.html',{'id':id})



def custaff(request):
  cr = staf.objects.all()
  return render(request,'custaff.html',{'cr':cr})

def detail(request,pk):
  cr = staf.objects.get(id = pk)
  return render(request,"detail.html",{'cr':cr})


def logout(request):
    logout(request)
    return redirect('login')

def update(request,pk):
   cr=staf.objects.get(id=pk)
   form=up(instance=cr)
   if request.method=="POST":
     form=up(request.POST,instance=cr)
     if form.is_valid:
       form.save()
     redirect('wel')
   return render(request,"update.html",{'form':form})  


   #adding jwellery#
def jead(request):
    if request.method == 'POST':
        form = im(request.POST, request.FILES)
 
        if form.is_valid():
            form.save()
            return redirect('wel')
    else:
        form = im()
    return render(request, 'jead.html', {'form': form})
 
   
  
  #jwellery view

def jwd(request):
  cr = jew.objects.all()
  return render(request,'jwd.html',{'cr':cr})

#delete jwellery

def dele(request,pk):
   cr = jew.objects.get(id =pk)
   cr.delete()
   return redirect("jwd")
#showing page
def show(request):
  cr = jew.objects.all()
  return render(request,'show.html',{'cr':cr})
#coustomer reg
def usreg(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        cus(name=name,email=email,password=password).save()
    return render (request,"usreg.html")
  
#customer login
def uslog(request):
    return render(request,'uslog.html')
#customer login
def ususer(request):
    if request.method== 'POST':
      email = request.POST.get('email')
      password = request.POST.get('password')
      cr = cus.objects.filter(email=email, password=password)
      if cr:
        user_details=cus.objects.get(email=email,password=password)
        id=user_details.id
        name=user_details.name
        request.session['id']=id
        request.session['name']=name

    
        return redirect('show')

      else:
        return render(request,'uslog.html')
    else:
        return render(request,'usreg.html')

def buy(request,pk):
  if request.method == "POST":
        name = request.POST.get('name')
        price = request.POST.get('price')
        pin = request.POST.get('pin')
        orid = request.POST.get('orid')
        orn = request.POST.get('orn')
        add = request.POST.get('add')
        pay = request.POST.get('pay')
        order(name=name,price=price,pin=pin,orid=orid,orn=orn,add=add,pay=pay).save()
  cr = jew.objects.get(id = pk)
  return render(request,"buy.html",{'cr':cr})
#payment
def pay(request):
    return render(request,'pay.html')

#card
def card(request):
  if request.method == "POST":
      pay = request.POST.get('pay')
      order(pay=pay).save()
  return render(request,'card.html')
#order details
def ord(request):
  cr = order.objects.all()
  return render(request,"ord.html",{'cr':cr})

#search

def search(request):
  if request.method == 'GET':
    search = request.GET.get('search')
    post = jew.objects.all().filter(mod=search)
    return render(request,'search.html',{'post':post})


#cart


  






 