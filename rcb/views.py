from django.shortcuts import render

# Create your views here.
def kholi(request):
     d={'name':'Virat Kholi','role':'Right hand batsman',"age":33}
     return render(request,'rcbprofile.html',context=d)
def duplessis(request):
     d={'name':'Faf du plessis','role':'Right hand batsman',"age":36}
     return render(request,'rcbprofile.html',context=d)
def abd(request):
     d={'name':'AB de villiers','role':'Right hand batsman',"age":35}
     return render(request,'rcbprofile.html',context=d)
def maxwell(request):
     d={'name':'Glenn Maxwell','role':'Right hand batsman',"age":33}
     return render(request,'rcbprofile.html',context=d)
def dk(request):
     d={'name':'Dinesh Karthik','role':'Wicket keeper and Right hand batsman',"age":39}
     return render(request,'rcbprofile.html',context=d)
def hasaranga(request):
     d={'name':'Wanindu Hasaranga','role':'right hand bowler and batsman',"age":33}
     return render(request,'rcbprofile.html',context=d)
def siraj(request):
     d={'name':'Mohammed Siraj','role':'Right hand bowler',"age":29}
     return render(request,'rcbprofile.html',context=d)
def allen(request):
     d={'name':'Finn Allen','role':'Right hand batsman',"age":28}
     return render(request,'rcbprofile.html',context=d)
def sharma(request):
     d={'name':'Karn Sharma','role':'Right hand bowler',"age":33}
     return render(request,'rcbprofile.html',context=d)

