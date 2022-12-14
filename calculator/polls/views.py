from django.shortcuts import render
# Create your views here.

def viewHome(request):
    return render(request, "home.html")




def viewAddition(request):
    weight = request.POST['weight']
    height = request.POST['height']
    age = request.POST['age']
    activityLevel = request.POST.get('activityLevel')
    sexo = request.POST.get('sexo')
    options_dict = {"Sedentários": 1.2, "Levemente ativo":1.375, "Moderadamente ativo":1.55, "Altamente ativo":1.725, "Extremamente ativo": 1.9}
    
    
    
    a = int(weight)
    b = int(height)
    c = int(age)
    
    if sexo == "masculino":
        resultBMR = round(options_dict.get(activityLevel) * (66 + (13.7 * a) + (5 * b) - (6.8 * c)))
       
    else:
        resultBMR = round(options_dict.get(activityLevel) * (655 + (9.6 * a) + (1.8 * b) - (4.7 * c)))
          
        
    resultCutting = resultBMR - 400
    resultBulking = resultBMR + 400        
        
    
    return render(request, "home.html", {"resultBMR": resultBMR, "resultCutting": resultCutting, "resultBulking": resultBulking, "sexo":sexo}) 
   

    
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
            mensagem = "Magreza Grave"
        elif resultIMC < 17:
            mensagem = "Magreza Moderada"
        elif resultIMC < 18.5:
            mensagem = "Magreza Leve"
        elif resultIMC < 25:
            mensagem = "Saudável"
        elif resultIMC < 30:
            mensagem = "Sobrepeso"
        elif resultIMC < 35:
            mensagem = "Obesidade Grau I"
        elif resultIMC < 40:
            mensagem = "Obesidade Grau II"
        else:
            mensagem = "Obesidade Grau III"
            
        return render(request, "home.html", {"resultIMC": resultIMC, "mensagem": mensagem } )    
  
