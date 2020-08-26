from django.shortcuts import render
from .models import Destination
# Create your views here.
def index(request):
    
    """"dest1=Destination()
    dest1.name="Mumbai"
    dest1.desc="The Dream City"
    dest1.price=700
    dest1.img='destination_1.jpg'
    dest1.offer=True """""  

    dests=Destination.objects.all()
    return render(request,"index.html",{'dests': dests})