from django.shortcuts import render
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import UserInfo


def IndexPage(request):
    return render(request,"index.html")
def LoginPage(request):
    return render(request,"Login.html")
def RegisterPage(request):
    return render(request,"Register.html")

def RegisterPage(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        gender = request.POST.get('gender')
        dob = request.POST.get('dob')
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        country = request.POST.get('country')
        zip_code = request.POST.get('zip_code')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        passw = request.POST.get('passw')
        
        
        # Create a new UserInfo instance
        my_userinfo = UserInfo(
            fname=fname,
            lname=lname,
            gender=gender,
            dob=dob,
            address=address,
            city=city,
            state=state,
            country=country,
            zip_code=zip_code,
            phone=phone,
            email=email,
            passw=passw,
            )
        my_userinfo.save()
        return render(request, 'index.html')
    else:
        return render(request, 'Register.html')
        

            




