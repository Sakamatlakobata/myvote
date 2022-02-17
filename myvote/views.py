from django.shortcuts import render
# from django.shortcuts import get_object_or_404
# import datetime
# from django.template  import loader
# from django.http      import HttpResponse, HttpResponseRedirect
# from django.urls      import reverse
# from django.views     import generic
# from django.utils     import timezone
# from .models          import Choice, Question

def menu_main(request):
    context = {'Heading':{
        'Bills and Legislative Process':{'Get Bill':'bill_vote/bill_get','Bills':'news/articles/2022','Representatives':'news/articles/2022','Voting':''},
        "People's Vote":{'Surveys':'polls','Questions':'polls','Reports':'polls'},
        'Discussion Boards':{'Boards':'boards',},
        'Meetups':{'Find district from ZIPcode':'meetup/district_get', 'Electoral district associations':'ridings','Meetings':'meetups',},
        'Government budget':{'Vote on budget items':'budgetItems',},
        'Maintenance tickets':{'Open ticket':'tickets','Vote on tickets':'ticketVote',},
        'User Accounts':{'Login page':'accounts/login','Register page':'accounts/register','Logout':'accounts/logout',},
    }}
    return render(request, 'myvote/menu_main.html', context)
