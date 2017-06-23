from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

from humshaugh_table_tennis.models import News
from humshaugh_table_tennis.forms import NewsForm

def home(request):
    return render(request, 'humshaugh_table_tennis/home.html')

def news(request, page):
    context_dict = {}
    page = int(page)
    news_count = News.objects.all().count()

    last_page = (news_count / 10) + 1
    
    if page < 1 or page != 1 and page > last_page:
        return HttpResponseRedirect(reverse('humshaugh_table_tennis:news', args=[1]))
        

    # show ten per page
    # u is upper bound
    # l is lower bound
    u = page * 10
    l = u - 10
    posts = News.objects.order_by('-date')[l:u]

    context_dict['last_page'] = last_page
    context_dict['page'] = page
    context_dict['posts'] = posts
    return render(request, 'humshaugh_table_tennis/news.html', context_dict)


def club_nights(request):
    return render(request, 'humshaugh_table_tennis/club_nights.html')

def contact_us(request):
    return render(request, 'humshaugh_table_tennis/contact_us.html')

def location(request):
    return render(request, 'humshaugh_table_tennis/location.html')

def rules(request):
    return render(request, 'humshaugh_table_tennis/rules.html')

def rules_full(request):
    return render(request, 'humshaugh_table_tennis/rules_full.html')



##def login(request):
##    context_dict = {}
##
##    if request.method == 'POST':
##        # check if username and password are valid
##        username = request.POST.get('username')
##        password = request.POST.get('password')
##
##        user = authenticate(username=username, password=password)
##
##        if user:
##            # check account is not disabled
##            if user.is_active:
##                # login the user and redirect to their profile
##                login(request, user)
##                return HttpResponseRedirect(reverse('humshaugh_table_tennis:manage'))
##
##            # inactive account
##            else:
##                context_dict['errors'] = ['Your account is disabled.']
##                return render(request, 'humshaugh_table_tennis/login.html', context_dict)
##
##        # invalid login details
##        else:
##            print('Invalid login details: {0}, {1}'.format(username, password))
##            context_dict['errors'] = ['Invalid login details']
##            return render(request, 'humshaugh_table_tennis/login.html', context_dict)
##        
##    else:
##        # Not HTTP POST
##        return render(request, 'humshaugh_table_tennis/login.html', context_dict)
##
##

    
