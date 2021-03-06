from django.shortcuts import render,redirect,get_object_or_404
from ..models import *

def FoodAddView(request):
    foods = Food.objects.all()
    if request.method == 'POST':
        name = request.POST['name']
        calories = request.POST['calories']
        proteins = request.POST['proteins']
        fats = request.POST['fats']
        carbo = request.POST['carbo']
        img = request.FILES.get('img')
        Food.objects.create(name=name,calories=calories,proteins=proteins,fats=fats,carbo=carbo,img=img)
        return redirect('food-add')
    context = {
        'foods':foods,
    }
    return render(request,'admin_panel/admin-food-add.html',context)

def FoodEditView(request,food_id):
    food = get_object_or_404(Food,pk=food_id)
    if request.method == 'POST':
        type = request.POST['form']
        if type == 'edit':
            name = request.POST['name']
            calories = request.POST['calories']
            proteins = request.POST['proteins']
            fats = request.POST['fats']
            carbo = request.POST['carbo']
            img = request.FILES.get('img')
            if img == None:
                food.name = name
                food.carbo = carbo
                food.calories = calories
                food.proteins = proteins
                food.fats = fats
                food.save()
                return redirect('food-edit',food_id)
            else:
                food.name = name
                food.carbo = carbo
                food.calories = calories
                food.proteins = proteins
                food.fats = fats
                food.img = img
                food.save()
                return redirect('food-edit',food_id)
        if type == 'delete':
            food.delete()
            return redirect('food-add')
    context = {
        'food':food
    }
    return render(request,'admin_panel/admin-food-edit.html',context)


def ExAddView(request):
    ex = Exercise.objects.all()
    if request.method == 'POST':
        name = request.POST['name']
        calories = request.POST['calories']
        time = request.POST['time']
        img = request.FILES.get('img')
        Exercise.objects.create(name=name,calories=calories,time=time,img=img)
        return redirect('ex-add')
    context = {
        'exe':ex,
    }
    return render(request,'admin_panel/admin-ex-add.html',context)

def ExEditView(request,ex_id):
    ex = get_object_or_404(Exercise,pk=ex_id)
    if request.method == 'POST':
        type = request.POST['form']
        if type == 'edit':
            name = request.POST['name']
            calories = request.POST['calories']
            time = request.POST['time']
            img = request.FILES.get('img')
            if img == None:
                ex.name = name
                ex.time = time
                ex.calories = calories
                ex.save()
                return redirect('ex-edit',ex_id)
            else:
                ex.name = name
                ex.time = time
                ex.calories = calories
                ex.img = img
                ex.save()
                return redirect('ex-edit',ex_id)
        if type == 'delete':
            ex.delete()
            return redirect('ex-add')
    context = {
        'ex':ex
    }
    return render(request,'admin_panel/admin-ex-edit.html',context)