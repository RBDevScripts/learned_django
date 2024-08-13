from django.shortcuts import render,redirect
from app.models import Reg

# Create your views here.
def home(request):
    return render(request,"home.html")
def about(request): 
    return render(request,"about.html")
def contact(request): 
    return render(request,"contact.html")
def product(request): 
    return render(request,"product.html")
def showUser(request):
    students=Reg.objects.all()
    context={
        'students':students
    }
    return render(request,"crud.html",context)
def delete(request,id):
    st=Reg.objects.get(id=id)
    st.delete()
    return redirect("crud-page")
def add(request):
    if request.method == 'POST':
        name = request.POST.get('pname')
        email = request.POST.get('email')
        dob = request.POST.get('dob')
        password = request.POST.get('pass')

        if name and email and dob and password:
            student = Reg(name=name,email=email,dob=dob,password=password)
            student.save()
            return redirect('crud-page')
        else:
            return render(request,"add.html")
    else:
        return render(request,"add.html")   

def update(request,id):
    student=Reg.objects.get(id=id)
    if request.method == 'POST':
        name = request.POST.get('pname')
        email = request.POST.get('email')
        dob = request.POST.get('dob')
        password = request.POST.get('pass')

        if name and email and dob and password:
            student.name = name
            student.email = email
            student.dob = dob
            student.password = password

            student.save()
            return redirect('crud-page')
    else:
        return render(request,"update.html",{'student':student})