import random,json
import pandas as pd
from django.core.urlresolvers import reverse
from itertools import chain
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate, login,logout
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.template import Context
from django.core import serializers
from django.db.models import Max
from .models import Question,Phpquestion,Userprof,ContactDetails,UserQuestions,Pythonquestion,Composition,Vocabulary,Document,studentprof,Dictation,Resources
from polls.forms import *
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect

def std(request):
    standard=request.POST.get('std')
    request.session['grade']=standard
    request.session['count']=1
    up = studentprof.objects.create(username=request.user.username)
    return render(request, 'test.html',{'stan':standard})


def test(request):
    return render(request, 'test.html')

def Compositionindex(request):
    if request.user.is_authenticated():
        cs=request.session['grade']
        print cs
        comp=list(Composition.objects.filter(std=str(cs)))
        print comp
        random.shuffle(comp)
        form=DocumentForm()
        jlist=comp[:1]
        request.session['jlist'] = [j.q_id for j in jlist]
        return render(request,'single_input.html',{'latest_question_list': jlist,'form':form})
    else:
        return HttpResponseRedirect('/')

def Compositionresult(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile = request.FILES['docfile'])
            newdoc.save()

            # Redirect to the document list after POST
            #return HttpResponseRedirect(reverse('myapp.views.list'))
    else:
        form = DocumentForm() # A empty, unbound form

    # Load documents for the list page
    documents = Document.objects.filter(docfile__contains=request.user.username)
    
    studentprof.objects.filter(username=request.user.username).update(handwriting=documents)
    # Render list page with the documents and the form
    return render_to_response(
        'pic.html',
        {'documents': documents, 'form': form}      
        
    )
def vocabindex(request):
    if request.user.is_authenticated():
        
        javapool = list(Vocabulary.objects.filter(std=request.session['grade']))
        random.shuffle(javapool)
        jlist = javapool[:4]
        request.session['jlist'] = [j.q_id for j in jlist]
        return render(request,'index.html',{'latest_question_list': jlist})
    else:
        return HttpResponseRedirect('/')

def vocabresult(request):
    
    if request.user.is_authenticated():
        ch = []
        correct = 0
        idlist = request.session['jlist']
        jlist = []
        for i in idlist:
            jlist.append(Vocabulary.objects.get(pk=i))
        answers = []
        for j in jlist:
            answers.append(j.ans)

        for i in range(1,4):
            s = request.POST.get(str(i))
            if s:
                question, choice = s.split('-')
                ch.append(choice)
            else:
                ch.append(None)

        for i in range(0,3):
            if ch[i] == answers[i]:
                correct+=1
        

            
        if(correct<=2):
            request.session['grade']=int(request.session['grade'])-1
            return HttpResponseRedirect('http://127.0.0.1:8000/test/vocabtest/')
        else:
            lisst = zip(jlist,ch)
        return render(request,'result.html',{'qlist':lisst,'score':correct})
    else:

        return HttpResponseRedirect('/')



def compreindex(request):
    if request.user.is_authenticated():
        phppool = list(Phpquestion.objects.all())
        random.shuffle(phppool)
        phplist = phppool[:10]
        request.session['phplist'] = [p.q_id for p in phplist]
        return render(request,'index.html',{'latest_question_list': phplist})
    else:
        return HttpResponseRedirect('/')

def compreresult(request):
    if request.user.is_authenticated():
        ch = []
        correct = 0
        idlist = request.session['phplist']
        phplist = []
        for i in idlist:
            phplist.append(Phpquestion.objects.get(pk=i))
        answers = []
        for p in phplist:
            answers.append(p.ans)

        for i in range(1,11):
            s = request.POST.get(str(i))
            if s:
                question, choice = s.split('-')
                ch.append(choice)
            else:
                ch.append(None)
        
        for i in range(0,10):
            if ch[i] == answers[i]:
                correct+=1

        lisst = zip(phplist,ch)

        up = Userprof.objects.create(username=request.user.username,subject='php',score=correct)

        return render(request,'result.html',{'qlist':lisst,'score1':correct})
    else:
        return HttpResponseRedirect('/')

def mathindex(request):
    if request.user.is_authenticated():
        pypool = list(Pythonquestion.objects.all())
        random.shuffle(pypool)
        pylist = pypool[:10]
        request.session['pylist'] = [p.q_id for p in pylist]
        return render(request,'index.html',{'latest_question_list': pylist})
    else:
        return HttpResponseRedirect('/')

def mathresult(request):
    if request.user.is_authenticated():
        ch = []
        correct = 0
        idlist = request.session['pylist']
        pylist = []
        for i in idlist:
            pylist.append(Pythonquestion.objects.get(pk=i))
        answers = []
        for p in pylist:
            answers.append(p.ans)

        for i in range(1,11):
            s = request.POST.get(str(i))
            if s:
                question, choice = s.split('-')
                ch.append(choice)
            else:
                ch.append(None)

        for i in range(0,10):
            if ch[i] == answers[i]:
                correct+=1

        lisst = zip(pylist,ch)

        up = Userprof.objects.create(username=request.user.username,subject='python',score=correct)

        return render(request,'result.html',{'qlist':lisst,'score2':correct})
    else:
        return HttpResponseRedirect('/')


def contact(request):
    form_class = ContactForm

    # new logic!
    if request.method == 'POST':
        form = form_class(data=request.POST)
        if form.is_valid():
            contact_name = request.POST.get('contact_name', '')
            contact_email = request.POST.get('contact_email', '')
            form_content = request.POST.get('content', '')
            FormObj = ContactDetails(username=contact_name,email=contact_email,content=form_content)
            FormObj.save()
            # Email the profile with the 
            # contact information
            template = get_template('polls/contact_template.txt')
            context = {'contact_name': contact_name,'contact_email': contact_email,'form_content': form_content,}
            content = template.render({'context':context})
            email = EmailMessage(
                "New contact form submission",
                content,
                "LDD" +'',
                ['quizzy2016@gmail.com'],
                headers = {'Reply-To': contact_email }
            )
            email.send()
            return HttpResponseRedirect('contact')
    return render(request, 'polls/contact.html', {'form': form_class,})

def submitq(request):
    form_class = QuestionForm

    # new logic!
    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get('contact_name', '')
            contact_email = request.POST.get('contact_email', '')
            form_content = request.POST.get('content', '')
            FormObj = UserQuestions(username=contact_name,email=contact_email,question=form_content)
            FormObj.save()

            # Email the profile with the 
            # contact information
            template = get_template('polls/question1.txt')
            context = {
                'contact_name': contact_name,
                'contact_email': contact_email,
                'form_content': form_content,
            }
            content = template.render({'context':context})
            email = EmailMessage(
                "User has Entered",
                content,
                "" +'',
                [''],
                headers = {'': contact_email }
            )
            email.send()
            return HttpResponseRedirect('/submitq')

    return render(request, 'polls/question.html', {'form': form_class,})


def handler404(request):
    return render(request,'404.html')

def handler500(request):
    return render(request,'500.html')

def dict(request):
    dictpool = list(Dictation.objects.all())
    dictlist=dictpool[:3]
    #print dictlist.word
    request.session['dlist']=[q.word for q in dictlist]
    return render(request,'dict.html',{'latest_question_list': dictlist})

def dictresult(request):
    c=[]
    correct=0
    ans=request.session['dlist']
    print ans
    for x in range(1,3):
        c.append(request.POST.get(str(x)))
        print c
    for i in range(0,2):
        if c[i]==ans[i]:
            correct+=1
    return render(request,'r1.html',{'score': correct})

def usertable(request):
    query_results = YourModel.objects.filter(status=p)
    return render(request,'table.html',{'query_results': query_results})

def count(request):
    request.session['count']=int(request.session['count'])+1
    if(request.session['count']==2):
        return HttpResponseRedirect('http://127.0.0.1:8000/test/compretest/')
    if(request.session['count']==3):
        return HttpResponseRedirect('http://127.0.0.1:8000/test/mathtest/')
    if(request.session['count']==4):
        return HttpResponseRedirect('http://127.0.0.1:8000/test/compositiontest/')
    if(request.session['count']==5):
        return HttpResponseRedirect('http://127.0.0.1:8000/test/dict/')
    if(request.session['count']==6):
        return HttpResponseRedirect('http://127.0.0.1:8000/test/ml/')  

def detect(request):
    
    student=pd.read_excel('student.xlsx', sheetname=0, header=0, skiprows=None, skip_footer=0, index_col=None, names=None, parse_cols=None, parse_dates=False, date_parser=None, na_values=None, thousands=None, convert_float=True, has_index_names=None, converters=None, true_values=None, false_values=None, engine=None, squeeze=False)
   
    student.columns=['std','wr','cmpr','sp','cr', 'comp','punc','hw', 'r','s','h','we','bm','hm','a','d','mem','mot','ss','ds','ll','sl','sll','rg','ld','rndm']
   
    student['s'].fillna(student['s'].mean(),inplace=True)
    student['h'].fillna(student['h'].mean(),inplace=True)
    student['we'].fillna(student['we'].mean(),inplace=True)
    student['bm'].fillna(student['bm'].mean(),inplace=True)
    student['a'].fillna(student['a'].mean(),inplace=True)
    student['d'].fillna(student['d'].mean(),inplace=True)
    student['mem'].fillna(student['mem'].mean(),inplace=True)
    student['mot'].fillna(student['mot'].mean(),inplace=True)
    student['ss'].fillna(student['ss'].mean(),inplace=True)
    student['ds'].fillna(student['ds'].mean(),inplace=True)
    student['ll'].fillna(student['ll'].mean(),inplace=True)
    student['sl'].fillna(student['sl'].mean(),inplace=True)
    student['sll'].fillna(student['sll'].mean(),inplace=True)
    student['rg'].fillna(student['rg'].mean(),inplace=True)
    student['hm'].fillna(student['hm'].mean(),inplace=True)
    student['r'].fillna(student['r'].mean(),inplace=True)
   
    X=student.iloc[::,8:24]
    y=student.iloc[::,24]
   
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y)
    
   
    from sklearn.neural_network import MLPClassifier
    mlp = MLPClassifier(hidden_layer_sizes=(16,16,16),max_iter=500)
    mlp.fit(X_train,y_train)
    instance = studentprof.objects.values('dr')[0]
    d1 = instance['dr']
    instance = studentprof.objects.values('ds')[0]
    d2 = instance['ds']
    instance = studentprof.objects.values('dh')[0]
    d3 = instance['dh']
    instance = studentprof.objects.values('dwe')[0]
    d4 = instance['dwe']
    instance = studentprof.objects.values('dba')[0]
    d5 = instance['dba']
    instance = studentprof.objects.values('dha')[0]
    d6 = instance['dha']
    instance = studentprof.objects.values('da')[0]
    d7 = instance['da']
    instance = studentprof.objects.values('ed')[0]
    d8 = instance['ed']
    instance = studentprof.objects.values('dm')[0]
    d9 = instance['dm']
    instance = studentprof.objects.values('lm')[0]
    d10 = instance['lm']
    instance = studentprof.objects.values('dss')[0]
    d11 = instance['dss']
    instance = studentprof.objects.values('dns')[0]
    d12 = instance['dns']
    instance = studentprof.objects.values('dll')[0]
    d13 = instance['dll']
    instance = studentprof.objects.values('dls')[0]
    d14 = instance['dls']
    instance = studentprof.objects.values('stl')[0]
    d15 = instance['stl']
    instance = studentprof.objects.values('rg')[0]
    d16 = instance['rg']

    abc=[[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
    #abc=[[d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11,d12,d13,d14,d15,d16]]
    
    predictions = mlp.predict(abc)
    #print predictions[0]
    request.session['ld']=int(predictions[0])
    if(request.session['ld']==1):
        return render(request,'detect.html',{'predictions':predictions})
    else:
        return render(request,'detect1.html',{'predictions':predictions})
    
def user(request):
    count=0
    c=[]
    std=2
    if(request.session['ld']==1):
        
        instance = studentprof.objects.values('dr')[0]
        d1 = instance['dr']
        if(d1<std):
            c.append("Reading")
            count=count+1
        instance = studentprof.objects.values('ds')[0]
        d2 = instance['ds']
        if(d2<std):
            c.append("Spelling")
            count=count+1
        instance = studentprof.objects.values('dwe')[0]
        d4 = instance['dwe']
        if(d4<std):
            c.append("Writing")
            count=count+1
        instance = studentprof.objects.values('dba')[0]
        d5 = instance['dba']
        if(d5<std):
            c.append("Maths")
            count=count+1
    areas=list(c)
    p=areas[:count]

    print p
    print count
    return render(request,'user.html',{'p':p})

def resource(request):
    r = request.GET['mat']
    print r
    instance = studentprof.objects.values(r)[0]
    s_grade = instance[r]
    obj=Resources.objects.filter(subject_grade=s_grade,area=r)
    print obj
    return render(request,'resource.html',{'r':r,'obj':obj})


    