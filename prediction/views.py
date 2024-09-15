from django.shortcuts import render
import pandas as pd
import numpy as np

#libraries for prediction
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,confusion_matrix

# Create your views here.
def home(request):
    return render(request,'home.html')

def prediction(request):
    return render(request, 'prediction.html')
def results(request):
   # Load your dataset
   data = pd.read_csv("/Users/Lenovo/Desktop/python_projects/diabetes.csv")
   print(data)
   x = data.drop("Outcome", axis=1)
   y = data["Outcome"]
   x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

   # Create a logistic regression model with max-iter to allow for more iterations.
   model = LogisticRegression(max_iter=1000)
   model.fit(x_train, y_train)

   if request.method == 'POST':
       val1 = float(request.POST['pregnancies'])
       val2 = float(request.POST['glucose'])
       val3 = float(request.POST['blood_pressure'])
       val4 = float(request.POST['skin_thickness'])
       val5 = float(request.POST['insulin'])
       val6 = float(request.POST['bmi'])
       val7 = float(request.POST['diabetes'])
       val8 = float(request.POST['age'])

       print(f"Values from form: {val1}, {val2}, {val3}, {val4}, {val5}, {val6}, {val7}, {val8}")

       predict = model.predict([[val1, val2, val3, val4, val5, val6, val7, val8]])
       result = ""
       if predict == [1]:
           result = "Positive"
       elif predict == [0]:
           result = "Negative"

       print(f"Prediction result: {result}")

       return render(request, "prediction.html", {"result2": result})

   # Handle the case when the form is not submitted
   return render(request, "prediction.html")
