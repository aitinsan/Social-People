from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect,render,get_object_or_404
from admin_panel.models import *

@login_required
def CaloriesView(request):
    calories_sum = 0
    rc_sum = 0
    if request.user.is_authenticated:
        uf = UserFood.objects.filter(owner=request.user)
        rc = get_object_or_404(UserRequestedCalories,owner=request.user)
        rc_sum = int(rc.calo)
        for u in uf:
            calories_sum += int(u.food.calories)
    food = Food.objects.all()
    uf = UserFood.objects.filter(owner=request.user)
    if request.method == 'POST':
        type = request.POST['form']
        if type == 'add':
            food_pk = request.POST['food_pk']
            f = get_object_or_404(Food,pk=food_pk)
            UserFood.objects.create(food=f,owner=request.user)
            return redirect('calories')
        if type == 'delete':
            userfood_pk = request.POST['uf_pk']
            ufka = get_object_or_404(UserFood,pk=userfood_pk)
            ufka.delete()
            return redirect('calories')
    context = {
        'food':food,
        'user_food':uf,
        'calories_sum':calories_sum,
        'rc_sum':rc_sum,
    }
    return render(request,'front/calories.html',context)
@login_required
def ExercisesView(request):
    exe = Exercise.objects.all()
    ux = UserExercises.objects.all()
    if request.method == 'POST':
        type = request.POST['form']
        if type == 'add':
            food_pk = request.POST['food_pk']
            f = get_object_or_404(Exercise,pk=food_pk)
            UserExercises.objects.create(ex=f,owner=request.user)
            return redirect('exercises')
        if type == 'delete':
            userfood_pk = request.POST['uf_pk']
            ufka = get_object_or_404(UserExercises,pk=userfood_pk)
            ufka.delete()
            return redirect('exercises')
    context = {
    'exe':exe,
    'user_exercises':ux,
    }
    return render(request,'front/exercises.html',context)

def mapView(request):
    context = {

    }
    return render(request,'front/map.html',context)

def EditView(request):
    context={

    }
    return render(request,'front/edit.html',context)

@login_required
def RecommendedView(request):
    food = Food.objects.all()
    sum = 0
    if request.method == 'POST':
        calo = request.POST['calories']
        i = 0
        for f in food:
            if(sum < int(calo) and sum + int(f.calories) > sum):
                sum += int(f.calories)
        try:
            user_reco = UserRequestedCalories.objects.get(owner=request.user)
        except UserRequestedCalories.DoesNotExist:
            user_reco = UserRequestedCalories.objects.create(owner=request.user,calo=calo)
            user_reco.calo = calo
            user_reco.save()
    context={

    }
    return render(request,'front/recommend.html',context)