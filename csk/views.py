from django.shortcuts import render

# Create your views here.
def dhoni(request):
    d={'name':'Mahendra Singh Dhoni','role':'wicketkeeper and Right hand batsman',"age":40}
    return render(request,'cskprofile.html',context=d)
def raina(request):
    d={'name':'Suresh Raina','role':'Left hand batsman',"age":35}
    return render(request,'cskprofile.html',context=d)
def ruturaj(request):
    d={'name':'Ruturaj Gaikwad','role':'Right hand batsman',"age":22}
    return render(request,'cskprofile.html',context=d)
def jadeja(request):
    d={'name':'Ravindra Jadeja','role':'Left hand batsman and bowler',"age":33}
    return render(request,'cskprofile.html',context=d)
def rayudu(request):
    d={'name':'Ambati Rayudu','role':'wicketkeeper and Right hand batsman',"age":35}
    return render(request,'cskprofile.html',context=d)
def stokes(request):
    d={'name':'Ben Stokes','role':'Left hand batsman and bowler',"age":34}
    return render(request,'cskprofile.html',context=d)
def chahar(request):
    d={'name':'Deepak chahar','role':'Right hand bowler',"age":28}
    return render(request,'cskprofile.html',context=d)
def dube(request):
    d={'name':'Shivam dube','role':'Left hand batsman',"age":29}
    return render(request,'cskprofile.html',context=d)