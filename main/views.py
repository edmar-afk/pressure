from django.shortcuts import render
from .models import Respondents
# Create your views here.


def homepage(request):
    first_year = Respondents.objects.filter(year_level='First Year').count()
    second_year = Respondents.objects.filter(year_level='Second Year').count()
    third_year = Respondents.objects.filter(year_level='Third Year').count()
    fourth_year = Respondents.objects.filter(year_level='Fourth Year').count()
    
    context = {
        'first_year': first_year,
        'second_year': second_year,
        'third_year': third_year,
        'fourth_year': fourth_year,
    }
    return render(request, 'index.html', context)


def first(request):

    if request.method == 'POST':

        subject = request.POST['subject']
        year_level = request.POST['year']

        new = Respondents(subject=subject, year_level=year_level)
        new.save()

    sub1 = Respondents.objects.filter(subject='JH101', year_level='First Year').count()
    sub2 = Respondents.objects.filter(subject='GEC 101', year_level='First Year').count()
    sub3 = Respondents.objects.filter(subject='GEC 102', year_level='First Year').count()
    sub4 = Respondents.objects.filter(subject='GEC 103', year_level='First Year').count()
    sub5 = Respondents.objects.filter(subject='IT 100', year_level='First Year').count()
    sub6 = Respondents.objects.filter(subject='IT 101', year_level='First Year').count()
    sub7 = Respondents.objects.filter(subject='IT 102', year_level='First Year').count()
    sub8 = Respondents.objects.filter(subject='PATHFIT 1', year_level='First Year').count()
    sub9 = Respondents.objects.filter(subject='NSTP 1', year_level='First Year').count()
    sub10 = Respondents.objects.filter(subject='GEC 104', year_level='First Year').count()
    sub11 = Respondents.objects.filter(subject='GEC 105', year_level='First Year').count()
    sub12 = Respondents.objects.filter(subject='GEC 106', year_level='First Year').count()
    sub13 = Respondents.objects.filter(subject='GEE 101', year_level='First Year').count()
    sub14 = Respondents.objects.filter(subject='GEM 101', year_level='First Year').count()
    sub15 = Respondents.objects.filter(subject='IT 103', year_level='First Year').count()
    sub16 = Respondents.objects.filter(subject='IT 104', year_level='First Year').count()
    sub17 = Respondents.objects.filter(subject='PATHFIT 2', year_level='First Year').count()
    sub18 = Respondents.objects.filter(subject='NSTP 2', year_level='First Year').count()
    
    
    context = {
        'sub1': sub1,
        'sub2': sub2,
        'sub3': sub3,
        'sub4': sub4,
        'sub5': sub5,
        'sub6': sub6,
        'sub7': sub7,
        'sub8': sub8,
        'sub9': sub9,
        'sub10': sub10,
        'sub11': sub11,
        'sub12': sub12,
        'sub13': sub13,
        'sub14': sub14,
        'sub15': sub15,
        'sub16': sub16,
        'sub17': sub17,
        'sub18': sub18,
    }
    return render(request, 'includes/1styear.html', context)








def second(request):

    if request.method == 'POST':

        subject = request.POST['subject']
        year_level = request.POST['year']

        new = Respondents(subject=subject, year_level=year_level)
        new.save()

    sub1 = Respondents.objects.filter(subject='GEE 201', year_level='Second Year').count()
    sub2 = Respondents.objects.filter(subject='GEC 201', year_level='Second Year').count()
    sub3 = Respondents.objects.filter(subject='IT 201', year_level='Second Year').count()
    sub4 = Respondents.objects.filter(subject='IT 202', year_level='Second Year').count()
    sub5 = Respondents.objects.filter(subject='IT 203', year_level='Second Year').count()
    sub6 = Respondents.objects.filter(subject='IT 204', year_level='Second Year').count()
    sub7 = Respondents.objects.filter(subject='PATHFIT 3', year_level='Second Year').count()
    sub8 = Respondents.objects.filter(subject='GEC 202', year_level='Second Year').count()
    sub9 = Respondents.objects.filter(subject='IT 205', year_level='Second Year').count()
    sub10 = Respondents.objects.filter(subject='IT 206', year_level='Second Year').count()
    sub11 = Respondents.objects.filter(subject='IT 207', year_level='Second Year').count()
    sub12 = Respondents.objects.filter(subject='IT 208', year_level='Second Year').count()
    sub13 = Respondents.objects.filter(subject='IT 209', year_level='Second Year').count()
    sub14 = Respondents.objects.filter(subject='PATHFIT 4', year_level='Second Year').count()
    
    
    
    context = {
        'sub1': sub1,
        'sub2': sub2,
        'sub3': sub3,
        'sub4': sub4,
        'sub5': sub5,
        'sub6': sub6,
        'sub7': sub7,
        'sub8': sub8,
        'sub9': sub9,
        'sub10': sub10,
        'sub11': sub11,
        'sub12': sub12,
        'sub13': sub13,
        'sub14': sub14,
    }
    return render(request, 'includes/2ndyear.html', context)











def third(request):

    if request.method == 'POST':

        subject = request.POST['subject']
        year_level = request.POST['year']

        new = Respondents(subject=subject, year_level=year_level)
        new.save()

    sub1 = Respondents.objects.filter(subject='GEC 301', year_level='Third Year').count()
    sub2 = Respondents.objects.filter(subject='IT 301', year_level='Third Year').count()
    sub3 = Respondents.objects.filter(subject='IT 302', year_level='Third Year').count()
    sub4 = Respondents.objects.filter(subject='IT 303', year_level='Third Year').count()
    sub5 = Respondents.objects.filter(subject='IT 304', year_level='Third Year').count()
    sub6 = Respondents.objects.filter(subject='IT 305', year_level='Third Year').count()
    sub7 = Respondents.objects.filter(subject='GEC 302', year_level='Third Year').count()
    sub8 = Respondents.objects.filter(subject='IT 306', year_level='Third Year').count()
    sub9 = Respondents.objects.filter(subject='IT 307', year_level='Third Year').count()
    sub10 = Respondents.objects.filter(subject='IT 308', year_level='Third Year').count()
    sub11 = Respondents.objects.filter(subject='IT 309', year_level='Third Year').count()
    sub12 = Respondents.objects.filter(subject='IT 310', year_level='Third Year').count()
    sub13 = Respondents.objects.filter(subject='IT 311', year_level='Third Year').count()
    sub14 = Respondents.objects.filter(subject='IT 312', year_level='Third Year').count()
    
    
    context = {
        'sub1': sub1,
        'sub2': sub2,
        'sub3': sub3,
        'sub4': sub4,
        'sub5': sub5,
        'sub6': sub6,
        'sub7': sub7,
        'sub8': sub8,
        'sub9': sub9,
        'sub10': sub10,
        'sub11': sub11,
        'sub12': sub12,
        'sub13': sub13,
        'sub14': sub14,
    }
    return render(request, 'includes/3rdyear.html', context)











def fourth(request):

    if request.method == 'POST':

        subject = request.POST['subject']
        year_level = request.POST['year']

        new = Respondents(subject=subject, year_level=year_level)
        new.save()

    sub1 = Respondents.objects.filter(subject='IT 401', year_level='Fourth Year').count()
    sub2 = Respondents.objects.filter(subject='IT 402', year_level='Fourth Year').count()
    sub3 = Respondents.objects.filter(subject='IT 403', year_level='Fourth Year').count()
    sub4 = Respondents.objects.filter(subject='IT 404', year_level='Fourth Year').count()
    sub5 = Respondents.objects.filter(subject='IT 405', year_level='Fourth Year').count()
    sub6 = Respondents.objects.filter(subject='IT 406', year_level='Fourth Year').count()
    sub7 = Respondents.objects.filter(subject='IT 407', year_level='Fourth Year').count()
   
    
    context = {
        'sub1': sub1,
        'sub2': sub2,
        'sub3': sub3,
        'sub4': sub4,
        'sub5': sub5,
        'sub6': sub6,
        'sub7': sub7,
       
    }
    return render(request, 'includes/4thyear.html', context)







