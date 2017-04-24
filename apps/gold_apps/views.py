# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime
from django.shortcuts import render, redirect
import random

def index(request):
    if 'gold' not in request.session.keys():
        request.session['gold'] = 0
    if 'history' not in request.session.keys():
        request.session['history'] = []    

    return render(request, 'gold_apps/index.html')

def process_money(request):
    choice = request.POST['building']
    print 'you picked', choice

    gold_earned = 0

    if choice == 'farm':
        gold_earned = random.randint(10, 20)
    elif choice == 'cave':
        gold_earned = random.randint(5, 10)
    elif choice == 'house':
        gold_earned = random.randint(2,5)
    elif choice == 'casino':
        gold_earned = random.randint(-50, 50)

    request.session['gold'] += gold_earned
    request.session['history'].append("Earned {} gold from the {} ({})".format(gold_earned, choice, datetime.now()))

    return redirect('/')

def reset(request):
    request.session.pop('gold')
    request.session.pop('history')
    return redirect('/')