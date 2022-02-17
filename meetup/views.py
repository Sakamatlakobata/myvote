from django.contrib.auth.decorators import login_required
from django.http      import HttpResponse
from django.shortcuts import render, redirect
from .forms           import GetZIPcode
from accounts.models  import Accounts
from django.contrib   import messages
import requests

# utility functions

# extract values from nested json
def json_extract(obj, key):
    arr = []
    def extract(obj, arr, key):
        """Recursively search for values of key in JSON tree."""
        if isinstance(obj, dict):
            for k, v in obj.items():
                if isinstance(v, (dict, list)):
                    extract(v, arr, key)
                elif k == key:
                    arr.append(v)
        elif isinstance(obj, list):
            for item in obj:
                extract(item, arr, key)
        return arr
    values = extract(obj, arr, key)
    return values

def get_member(ZIPcode):
    endpoint = "https://api.geocod.io/v1.7/geocode"
    params = {  'api_key':'b12b4b2046b214a066a2363130b422b63a26222',
                'fields':'cd', # congressional district
                'q':ZIPcode,}
                # 'q':form.cleaned_data['ZIPcode'],}
    response = requests.get(endpoint, params=params)
    # print('length of response', len(response.text), '[', response.text, ']')
    if response.text.find('error') > 0:
        context = response.json()
    else:
        last_name       = json_extract(response.json(),'last_name'     )[0] # 0 = congress, 1,2 = senators
        first_name      = json_extract(response.json(),'first_name'    )[0]
        bioguide_id     = json_extract(response.json(),'bioguide_id'   )[0] # member ID
        govtrack_id     = json_extract(response.json(),'govtrack_id'   )[0] 
        thomas_id       = json_extract(response.json(),'thomas_id'     )[0]
        opensecrets_id  = json_extract(response.json(),'opensecrets_id')[0]
        votesmart_id    = json_extract(response.json(),'votesmart_id'  )[0]
        icpsr_id        = json_extract(response.json(),'icpsr_id'      )[0]
        phone           = json_extract(response.json(),'phone'         )[0]
        bioguide_url    = 'https://www.govtrack.us/congress/members/'  + bioguide_id
        govtrack_url    = 'https://www.govtrack.us/congress/members/'  + govtrack_id
        opensecrets_url = 'https://www.opensecrets.org/search?q='      + opensecrets_id
        votesmart_url   = 'https://justfacts.votesmart.org/candidate/' + votesmart_id
        icpsr_url       = 'https://voteview.com/person/'               + icpsr_id
        context = { 'last_name'      :last_name,
                    'first_name'     :first_name,
                    'bioguide_id'    :bioguide_id,
                    'bioguide_url'   :bioguide_url,
                    'govtrack_id'    :govtrack_id,
                    'govtrack_url'   :govtrack_url,
                    'thomas_id'      :thomas_id,
                    'opensecrets_id' :opensecrets_id,
                    'opensecrets_url':opensecrets_url,
                    'votesmart_id'   :votesmart_id,
                    'votesmart_url'  :votesmart_url,
                    'icpsr_id'       :icpsr_id,
                    'icpsr_url'      :icpsr_url,
                    'phone'          :phone,
                    'ZIPcode'        :ZIPcode,}
                    # 'ZIPcode'        :form.cleaned_data['ZIPcode'],}
    return context


# views functions

# return member of congress for ZIPcode
# @login_required(login_url='/accounts/login/')
def district_get(request):
    if request.method == "POST":
        form = GetZIPcode(request.POST)
        if form.is_valid():
            context = get_member(form.cleaned_data['ZIPcode'])
            return render(request, 'meetup/district_display.html', context)

    if request.user.is_authenticated: # if logged in get ZIPcode from account
        zipcode = Accounts.objects.filter(user=request.user)[0].zipcode
        context = get_member(zipcode)
        return render(request, 'meetup/district_display.html', context)

    return render(request, 'meetup/district_get.html', {'form':GetZIPcode()})


def district_display(request):
    return HttpResponse(request)

