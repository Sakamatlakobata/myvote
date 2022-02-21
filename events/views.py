import calendar
import datetime
from   django.shortcuts import render
from   django.http      import HttpResponse
from   calendar         import HTMLCalendar
from   events.models    import Event

def calendar(request):
    today = datetime.date.today()
    month = datetime.date.strftime(today, '%b')
    year  = today.year
    title = "Event Calendar - %s %s" % (month, year)
    return HttpResponse("<H1>%s</H1>" % title)

def calendate(request, year, month):
    year  = int(year)
    month = int(month)
    if year < 1900 or year > 2099: year = datetime.date.today().year
    datetime_object = datetime.datetime.strptime(str(month), "%m")
    month_name = datetime_object.strftime("%b")
    # month_name = calendar.month_name[2]
    cal   = HTMLCalendar().formatmonth(year, month)
    title = "Event Calendar - %s %s" % (month_name, year)
    # return HttpResponse("<h1>%s</h1><p>%s</p>" % (title, cal))
    return render(request, "events/calendate.html", {"title":title,"cal":cal})

def event_list(request):
    event_list = Event.objects.all()
    return render(request, 'events/event_list.html', {"event_list":event_list,"title":"All Events"})
