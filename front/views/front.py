from django.shortcuts import redirect,get_object_or_404,render
from admin_panel.models import *

def FrontPage(request):
    uf = None
    ux = None
    calories_sum = 0
    carbo_sum = 0
    fats_sum = 0
    proteins_sum = 0
    ex_calo = 0
    if request.user.is_authenticated:
        uf = UserFood.objects.filter(owner=request.user)
        ux = UserExercises.objects.filter(owner=request.user)

        for u in uf:
            calories_sum += int(u.food.calories)
            proteins_sum += int(u.food.proteins)
            carbo_sum += int(u.food.carbo)
            fats_sum += int(u.food.carbo)
        for s in ux:
            ex_calo += int(s.ex.calories)
    total_calo = ex_calo + 700
    context = {
        'uf':uf,
        'ux':ux,
        'calories_sum':calories_sum,
        'proteins_sum':proteins_sum,
        'carbo_sum':carbo_sum,
        'fats_sum':fats_sum,
        'ex_calo':ex_calo,
        'total_calo':total_calo,
    }
    return render(request,'front/index.html',context)