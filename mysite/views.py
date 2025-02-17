from django.http  import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from mysite.form import Userform
def homepage(request):

     data={

         'title':"Page Title",

      'content':"Welcome to the homepage.",

      'course': ['python','django','html'],

      'students':[{'name':'Raj','age':25},

      {'name':'rahul','age':26}],

      'numbers':[1,2,3,4,5,6,7,8,9,10],

  }
     return render(request,"index.html",data)
def About(request):
    if request.method=='GET':
        output=request.GET.get('output')
    return render(request,"about.html",{'output':output})
def submitform (request):
    finalans=0
    data={}
    try:
     if request.method=='POST':
        name=request.POST.get('name')
        fname=request.POST.get('fname')
        finalans=name+fname
        data={
            'name':name,
            'fname':fname,
            'output':finalans,
        }
    except:
          pass

    return HttpResponse(finalans)
def contact(request):
    return render(request,"contact.html")
def menu(request):
    return render(request,"menu.html")
def home(request):
    return render(request,"home.html")
def userform(request):
        finalans=0
        fn=Userform()
        data={
            'form':fn
        }
        try:
          if request.method=='POST':
           name=request.POST.get('name')
           fname=request.POST.get('fname')
           finalans=name+fname
           data={
            
              'name':name,
              'fname':fname,
              'output':finalans,
              'form':fn,
        }
           url='/about/?output={}'.format(finalans)
           return redirect(url)
        except:
            pass  
        return render(request,"userform.html",data)
def calculator(request):
  data={}
  try:
    if request.method=='POST':
        num1=request.POST.get('num1')
        num2=request.POST.get('num2')
        opr=request.POST.get('opr')
        if opr=='+':
            ans=int(num1)+int(num2)
        elif opr=='-':
            ans=int(num1)-(num2)
        elif opr=='*':
            ans=int(num1)*(num2)
        else:
            ans=int(num1)/(num2)
        data={
            'num1':num1,
            'num2':num2,
            'opr':opr,
            'ans':ans
        }
  except:
    pass
  return render(request,"calculator.html",data)
def evenodd(request):
    data={}
    try:
        if request.method=="POST":
            if request.POST.get('num1')=="":
              return render(request,"evenodd.html",{'error':True})
            num1=request.POST.get('num1')       
            if int(num1)%2==0:
                c="Even"
            elif int(num1)%2!=0:
                c="Odd"
            else:
                c="invalid number" 
            data={
                'num1':num1,
                'c':c,
            }
    except:
        pass
    return render(request,"evenodd.html",data)
def marksheet(request):
    data={}
    Total_Marks=600
    try:
        if request.method=="POST":
            DSA=request.POST.get('dsa')
            print('DSA =====================',DSA)
            Linear=request.POST.get('linear')
            print('Linear =====================',Linear)
            CS=request.POST.get('cs')
            print('CS =====================',CS)
            Pakstudy=request.POST.get('pakstudy')
            print('Pakstudy =====================',Pakstudy)
            Arabic=request.POST.get('arabic')
            print("Arabic ======================",Arabic)
            SRE=request.POST.get('sre')
            print("SRE ======================",SRE)
            Obtained_Marks=int(DSA)+int(Linear)+int(CS)+int(Pakstudy)+int(Arabic)+int(SRE)
            Percentage=(Obtained_Marks/Total_Marks)*100
            if Percentage >= 80:
                Grade="A+"
            elif Percentage >= 70 and Percentage < 80:
                Grade="A"
            elif Percentage >= 60 and Percentage < 70:
                Grade="B"
            elif Percentage >= 50 and Percentage < 60:
                Grade="C"
            elif Percentage >= 40 and Percentage < 50:
                Grade="D"
            else:
                Grade="Fail"
            data={
                'Obtained_Marks':Obtained_Marks,
                'Percentage': round(Percentage, 2),
                'Grade':Grade
            }
    except Exception as e:
        pass

    return  render( request,"marksheet.html",data)


