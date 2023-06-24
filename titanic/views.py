import numpy as np
from django.shortcuts import render
import pickle
import os

def home(request):
    filename = os.path.abspath('titanic/model.pkl')
    model = pickle.load(open(filename, 'rb'))
    percent = 0
    if (request.method == 'POST'):
        pclass = request.POST['pclass']
        sex = request.POST['sex']
        age = request.POST['age']
        sibsp = request.POST['sibsp']
        parch = request.POST['parch']
        fare = request.POST['fare']
        embarked = request.POST['embarked']
        print(pclass,sex,age,sibsp,parch,fare,embarked)
        try:
            percent = model.predict_proba(np.array([[pclass,sex,age,sibsp,parch,fare,embarked]]))[0][1]
        except:
            percent = "Enter appropriate values"
    print("answer:",percent)
    if type(percent)==str:
        return render(request,"home.html",{'survival_rate':percent})
    else:
        return render(request, "home.html", {'survival_rate': str(percent*100)+'%'})


