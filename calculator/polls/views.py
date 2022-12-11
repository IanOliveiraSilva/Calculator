from django.shortcuts import render

# Create your views here.

def viewHome(request):
    return render(request, "home.html")

def viewAddition(request):
    numberOne = request.POST['numberOne']
    numberTwo = request.POST['numberTwo']
    
    if numberOne.isdigit() and numberTwo.isdigit():
        a = int(numberOne)
        b = int(numberTwo)
        result = a + b
        return render(request, "result.html", {"result": result})    
    else:
        result = "Only digits are allowed"
        return render(request, "result.html", {"result": result}) 
    
def viewSubtraction(request):
    numberOne = request.POST['numberOne']
    numberTwo = request.POST['numberTwo']
    
    if numberOne.isdigit() and numberTwo.isdigit():
        a = int(numberOne)
        b = int(numberTwo)
        result = a - b
        return render(request, "result.html", {"result": result})    
    else:
        result = "Only digits are allowed"
        return render(request, "result.html", {"result": result})    

def viewDivision(request):
    numberOne = request.POST['numberOne']
    numberTwo = request.POST['numberTwo']
    
    if numberOne.isdigit() and numberTwo.isdigit():
        a = int(numberOne)
        b = int(numberTwo)
        result = a / b
        return render(request, "result.html", {"result": result})    
    else:
        result = "Only digits are allowed"
        return render(request, "result.html", {"result": result})       

def viewMultiplication(request):
    numberOne = request.POST['numberOne']
    numberTwo = request.POST['numberTwo']
    
    if numberOne.isdigit() and numberTwo.isdigit():
        a = int(numberOne)
        b = int(numberTwo)
        result = a * b
        return render(request, "result.html", {"result": result})    
    else:
        result = "Only digits are allowed"
        return render(request, "result.html", {"result": result})    
    
       
