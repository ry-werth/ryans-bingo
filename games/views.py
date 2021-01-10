from django.http import Http404
from django.shortcuts import render
from django.template.defaulttags import register
import numpy as np
import random

@register.filter
def get_range(value):
    return range(value)

def generate_card_data(seed):
    data = []
    col_b = list(range(1,16))
    col_i = list(range(16,31))
    col_n = list(range(31,46))
    col_g = list(range(46,61))
    col_o = list(range(61,76))
    col_list = [col_b, col_i, col_n, col_g, col_o]
    for col in range(5):
        c = col_list[col]
        num_list = []
        for row in range(5):
            random.seed(seed)
            random_index = random.randint(0,len(c)-1)
            number = c[random_index]

            del c[random_index]

            num_list.append(number)

            seed += 1
        num_list.sort()
        data.append(num_list)


    return(np.transpose(data))
    # return(data)

def cardView(request, card_number=None):

    if card_number == 0:
        card_number=random.randint(1,101)

    card_data = generate_card_data(card_number)
    print(card_data)

    data = {"card_number":card_number, "card_data": card_data}
    return render(request, 'games/card.html', data)

def landing(request):
    return render(request, 'games/landing.html')

def caller(request):
    return render(request, 'games/caller.html')
