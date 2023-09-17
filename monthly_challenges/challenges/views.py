from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


# def challenge(request):
    # return HttpResponse("this works !")
# def january(request):
#     return HttpResponse("Eat no candy !")
# def february(request):
#     return HttpResponse("Work out for at least 1 hour!")
monthly_challenges = { 'january':'dont eat trash',
                      'february' : 'exercise daily'
                      'march' : 'be good person'
                      'april' : 'walk green'
                      'may' : 'scooping'}


def monthly_challenge(request, month):
    challenge_text = None
    if month == 'january':
        challenge_text = 'dont eat trash, dont be glutonous'
    elif month == 'february':
        challenge_text = 'exercise daily, dont be lazy'
    else:
        return HttpResponseNotFound
    return HttpResponse(challenge_text)

def  monthly_challenge_by_number(request, month):
    return HttpResponse (month)


