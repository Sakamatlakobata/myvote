"""myvote URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.views.generic    import RedirectView
from django.contrib          import admin
from django.urls             import path, include
from django.conf             import settings
from django.conf.urls.static import static
from myvote                  import views as myvote
from bill_vote               import views as bill_vote
from meetup                  import views as meetup
from accounts                import views as accounts
from events                  import views as events


''' can also maintain templates/base/base_site.html '''
admin.site.site_header = 'myVote'              # default: "Django Administration"
admin.site.index_title = 'Data administration' # default: "Site administration"
admin.site.site_title  = 'HTML title'          # default: "Django site admin"


urlpatterns = [

    path('admin/', admin.site.urls),
    path('',       myvote.menu_main, name='menu_main'), # site menu

    path('bill_vote/bill_get/', bill_vote.bill_get, name="bill_get"),

    path('meetup/district_get/',     meetup.district_get,     name="district_get"),
    path('meetup/district_display/', meetup.district_display, name="district_display"),

    path('accounts/login/',    accounts.loginPage,    name="accounts_login"),
    path('accounts/register/', accounts.registerPage, name="accounts_register"),
    path('accounts/logout/',   accounts.logoutUser,   name="accounts_register"),

    path('events/calendar/',               events.calendar,   name="events_calendar"),
    path('events/<int:year>/<int:month>/', events.calendate,  name="events_calendar_date"),
    path('events/event_list/',             events.event_list, name="event_list"),

#    path('', RedirectView.as_view(url='bill_discuss/', permanent=True)),

    # apps
#    path('bill_discuss/', include('bill_discuss.urls')),
    # path('bill_vote/',    include('bill_vote.urls')),
#    path('meetup/',       include('meetup.urls')),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

