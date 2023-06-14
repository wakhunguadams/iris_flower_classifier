from django.shortcuts import render
import numpy as np
import joblib

cls=joblib.load('final_model.sav')
# Create your views here.
def home_page(request):
    if request.method == "POST":
        
        x=[]
        x.append(request.POST['sl'])
        x.append(request.POST['sw'])
        x.append(request.POST['pl'])
        x.append(request.POST['pw'])
        print(x)

        y_pred=cls.predict([x])
        
        if y_pred[0] == 0:
            y_pred = "setosa"
        elif y_pred[0] == 1:
            y_pred = "verscicolor"
        else:
            y_pred = "virginica"
        return render(request,'home.html',{"result": y_pred})
    return render(request, 'home.html')
