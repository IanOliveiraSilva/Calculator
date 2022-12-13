from django.shortcuts import render
# Create your views here.

def viewHome(request):
    return render(request, "home.html")

def viewAddition(request):
    weight = request.POST['weight']
    height = request.POST['height']
    age = request.POST['age']
    a = int(weight)
    b = int(height)
    c = int(age)
    resultBMR = 1.55 * (66 + (13.7 * a) + (5 * b) - (6.8 * c))
    resultCutting = resultBMR - 400
    resultBulking = resultBMR + 400
    return render(request, "home.html", {"resultBMR": resultBMR, "resultCutting": resultCutting, "resultBulking": resultBulking})    

    
def viewSubtraction(request):
    weight = request.POST['weight']

    if weight.isdigit():
        a = int(weight)
        resultWater = (a * 35) / 1000
        
        return render(request, "home.html", {"resultWater": resultWater})    
    else:
        resultWater = "Only digits are allowed"
        return render(request, "home.html", {"resultWater": resultWater})    


def viewDivision(request):
    weight = request.POST['weight']

    if weight.isdigit():
        a = int(weight)
        resultProtein = a * 0.8
        return render(request, "home.html", {"resultProtein": resultProtein})    
    else:
        resultProtein = "Only digits are allowed"
        return render(request, "home.html", {"resultProtein": resultProtein})       

def viewMultiplication(request):
    weight = request.POST['weight']

    if weight.isdigit():
        a = int(weight)
        resultCarbs = a
        return render(request, "home.html", {"resultCarbs": resultCarbs})    
    else:
        resultCarbs = "Only digits are allowed"
        return render(request, "home.html", {"resultCarbs": resultCarbs})    
    

def viewFat(request):
    weight = request.POST['weight']

    if weight.isdigit():
        a = int(weight)
        resultFat = a * 0.4
        return render(request, "home.html", {"resultFat": resultFat})    
    else:
        resultFat = "Only digits are allowed"
        return render(request, "home.html", {"resultFat": resultFat})    
       
def viewIMC(request):
    weight = request.POST['weight']
    height = request.POST['height']


    if weight.isdigit():
        a = float(weight)
        b = float(height)
        resultIMC = a / b**2
        resultIMC = round(resultIMC, 2)
        
        if resultIMC < 16:
            mensagem = "Severe Thinness"
        elif resultIMC < 17:
            mensagem = "Moderate Thinness"
        elif resultIMC < 18.5:
            mensagem = "Mild Thinness"
        elif resultIMC < 25:
            mensagem = "Normal"
        elif resultIMC < 30:
            mensagem = "Overweight"
        elif resultIMC < 35:
            mensagem = "Obese Class I"
        elif resultIMC < 40:
            mensagem = "Obese Class II"
        else:
            mensagem = "Obese Class III"
            
        return render(request, "home.html", {"resultIMC": resultIMC, "mensagem": mensagem } )    
  
