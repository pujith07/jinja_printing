from django.shortcuts import render

# Create your views here.
# Create your views here.
def rohit(request):
     d={'name':'Rohit Sharma','role':'Right hand batsman',"age":34}
     return render(request,'miprofile.html',context=d)
def yadav(request):
     d={'name':'SuryaKumar Yadav','role':'Right hand batsman',"age":30}
     return render(request,'miprofile.html',context=d)
def pollard(request):
     d={'name':'Kieron Pollard','role':'Right hand batsman',"age":37}
     return render(request,'miprofile.html',context=d)
def brevis(request):
     d={'name':'Dewald Brevis','role':'Right hand batsman',"age":24}
     return render(request,'miprofile.html',context=d)
def kishan(request):
     d={'name':'Ishan Kishan','role':'Wicket keeper and Right hand batsman',"age":25}
     return render(request,'miprofile.html',context=d)
def david(request):
     d={'name':'Tim David','role':'right hand bowler and batsman',"age":30}
     return render(request,'miprofile.html',context=d)
def archer(request):
     d={'name':'Jofra Archer','role':'Right hand bowler',"age":31}
     return render(request,'miprofile.html',context=d)
def bumrah(request):
     d={'name':'Jasprit Bumrah','role':'Right hand bowler',"age":31}
     return render(request,'miprofile.html',context=d)
def sams(request):
     d={'name':'Daniel Sams','role':'left hand batsman and Bowler',"age":28}
     return render(request,'miprofile.html',context=d)
def mills(request):
     d={'name':'Timal Mills','role':'left hand bowler',"age":33}
     return render(request,'miprofile.html',context=d)

