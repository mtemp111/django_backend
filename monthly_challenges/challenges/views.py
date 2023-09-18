from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

# def challenge(request):
    # return HttpResponse("this works !")
# def january(request):
#     return HttpResponse("Eat no candy !")
# def february(request):
#     return HttpResponse("Work out for at least 1 hour!")
monthly_challenges = { 'january':'dont eat trash',
                      'february' : 'exercise daily',
                      'march':'be good person',
                      'april' : 'walk green',
                      'may' : 'scooping'}


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request,'challenges/challenge.html',{'text':challenge_text,
        'month_name':month})
    except:
        return HttpResponseNotFound('This month not supported')
def index(request):
    months = list(monthly_challenges.keys())
    return render(request,'challenges/index.html',{
        'months':months})
    

def  monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound('invalid months')
    forward_month = months[month-1]
    # return HttpResponse (monthly_challenges[forward_month])
    redirect_path = reverse('month-challenge', args= [forward_month])
    return HttpResponseRedirect(redirect_path)


