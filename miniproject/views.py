from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.db.models import Q
from .models import Phdtable
from django.http import HttpResponse
from django.views import View
from django.template.loader import get_template
from io import BytesIO
import xhtml2pdf.pisa as pisa
# Create your views here.
def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return render(request,'thesis.html')
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('login')
    else:
        return render(request,'login.html')

def register(request):
    
    if request.method == 'POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'User taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email taken')
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
               # user = User.objects.create()
                user.is_active = False
                user.save();
                return redirect('login')    
        else:
            messages.info(request,'password not matching.....')
            return redirect('register')
            
        #return redirect('/')
    else:
        return render(request,'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def thesis(request):
    
    student_name=request.POST.get("student_name")
    supervisor_name=request.POST.get("supervisor_name")
    thesis_title=request.POST.get("thesis_title")
    submission_year=request.POST.get("submission_year")
    department=request.POST.get("department")

    thesis_obj=Phdtable(student_name=student_name,supervisor_name=supervisor_name,thesis_title=thesis_title,submission_year=submission_year,department=department)
    thesis_obj.save()
    
    return render(request,'register.html')
"""
def info(request):
    dets=Phdtable.objects.all()
    return render(request,"info.html",{'dets': dets})
"""
query=None
def info(request):
    questions=None
    global query
    
    answer = request.POST.get('field')
    
    if answer=='all':
        query=Phdtable.objects.all().filter(Q(student_name=student_name))
    elif answer=="student_name":
        query=Phdtable.objects.all().filter(Q(student_name=student_name))
    elif answer=="supervisor_name":
        query=Phdtable.objects.all().filter(Q(supervisor_name=supervisor_name))
    elif answer=="thesis_title":
        query=Phdtable.objects.all().filter(Q(thesis_title=thesis_title))
    
    
    return render(request, 'info.html',{'query': query})




def render_to_pdf(template_src, context_dict={}):
	template = get_template(template_src)
	html  = template.render(context_dict)
	result = BytesIO()
	pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
	if not pdf.err:
		return HttpResponse(result.getvalue(), content_type='application/pdf')
	return None


#query=Phdtable.objects.all()
#Opens up page as PDF
class ViewPDF(View):
	def get(self, request, *args, **kwargs):

		pdf = render_to_pdf('infopdf.html', {'query': query})
		return HttpResponse(pdf, content_type='application/pdf')


#Automaticly downloads to PDF file
class DownloadPDF(View):
	def get(self, request, *args, **kwargs):
		
		pdf = render_to_pdf('infopdf.html', {'query': query})

		response = HttpResponse(pdf, content_type='application/pdf')
		filename = "Invoice_%s.pdf" %("12341231")
		content = "attachment; filename='%s'" %(filename)
		response['Content-Disposition'] = content
		return response



def index1(request):
	return render(request, 'index1.html')