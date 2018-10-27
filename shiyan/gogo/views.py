from django.shortcuts import render

# Create your views here.
def loginPage(request):
    return render(request, "long.html")
def loginPage2(request):
    return render(request, "have.html")

def show(request):
    from gogo import models
    if request.method == 'POST':
        a_user = request.POST['a_user']
        a_pwd = request.POST['a_pwd']
        models.userinfo.objects.create(name=a_user,pwd=a_pwd)
    user_list = models.userinfo.objects.all()
    return render(request,'have.html',{'user_list':user_list})


