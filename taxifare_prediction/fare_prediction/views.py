import joblib
from django.shortcuts import render
from django.http import JsonResponse

# Load the model (ensure the path is correct)
model = joblib.load('D:/taxi_fare_model.pkl')

def predict_fare(request):
    if request.method == 'POST':
        pickup_longitude = float(request.POST.get('pickup_longitude'))
        pickup_latitude = float(request.POST.get('pickup_latitude'))
        dropoff_longitude = float(request.POST.get('dropoff_longitude'))
        dropoff_latitude = float(request.POST.get('dropoff_latitude'))
        passenger_count = int(request.POST.get('passenger_count'))

        features = [[pickup_longitude, pickup_latitude, dropoff_longitude, dropoff_latitude, passenger_count]]
        prediction = model.predict(features)
        
        return JsonResponse({'fare': prediction[0]})

    return render(request, 'prediction/predict.html')
