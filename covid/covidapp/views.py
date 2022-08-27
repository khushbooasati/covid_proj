import string
from django.shortcuts import render
from pytz import country_names

import requests
import json

API_URL = "https://covid-193.p.rapidapi.com/"
HEADER = {
    "X-RapidAPI-Key": "baed117d64mshf0dbf33e7cd7abbp1b7f5fjsnc58cec6eab57",
    "X-RapidAPI-Host": "covid-193.p.rapidapi.com"
}

def helloworldview(request):
    if request.method == "GET":
        context = {}
        end_point = 'countries'
        response = requests.request("GET", API_URL + end_point, headers=HEADER).json()
        context['country_list'] = response['response']
        context['country_details'] = None


    if request.method == "POST":
        selectedcountry = request.POST.get("selectedcountry")
        print("selectedcountry:", selectedcountry)
        if selectedcountry:
            end_point = 'statistics'
            context = {}
            response = requests.request("GET", API_URL + end_point, headers=HEADER).json()
            context['statistics'] = response['response']
            for c_s in context['statistics']:
                if c_s['country'] == selectedcountry:
                    context['country_details'] = c_s
                    break
                    
    return render(request, 'helloworld.html', context)


    for country in range(0,len(context['country_list'])):
        if selectedcountry==response['response'][x]['country']:
            new = response['response'][x]['cases']['new']
            active = response['response'][x]['cases']['active']
            critical = response['response'][x]['cases']['critical']
            recovered = response['response'][x]['cases']['recovered']
            total = response['response'][x]['cases']['total']
            death = int(total) - int(active) -int(recovered)

