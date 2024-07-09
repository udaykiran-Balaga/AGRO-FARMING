from django.shortcuts import render
import serial
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from joblib import load
import joblib
import pandas as pd
import pickle

# Create your views here.
def machinelearning(request):
    return render(request,'machinelearning.html')
# def esp8266(request):
#     return render(request,'esp8266.html')
data11=[]
# @csrf_exempt
# def esp8266_endpoint(request):
    
#     if request.method == 'POST':
#         data = request.POST.get('data')
#        # Process the recieved data
#         print(f"Recieved data from ESP8266: {data}")
#     #     data1 = { 'data':data
#         #data1=data
#         data=int(data)
#         print(type(data))
#         # 
#         #
#         if data11:
#             data11.pop()  
#         data11.append(data)
#         print(data11)
#     #    }
#         return HttpResponse(data11)
#     print(data11)
#         # data11 = request.POST['data']
#         #return JsonResponse({'status':'only POST method is allowed'})
#     return HttpResponse(data11)  
def home(request):
    return render(request,'base.html')

@csrf_exempt
def serial_communication(request):
    if request.method == 'GET':
        try:
            # Open serial port
            ser = serial.Serial('COM4', 9600)  # Adjust port name accordingly
            # data = request.POST.get('data', '')
            # data = request.get('data', '')
            ser.write(89)
            # response_data = ser.readline().decode().strip()
        #     response_data = ser.readline().strip().decode('latin-1')
        # #     ser.close()
        #     data1={
        #         'response': response_data,
        #     }
        #     print(response_data)
        #     return render(request,'base.html',context=data1)
        #     # return JsonResponse({'response': response_data})
        # except Exception as e:
        #     return JsonResponse({'error': str(e)})
            # motor_speed=1000
            # ser.write(f"WaterPump:{motor_speed}\n".encode())
            ser.close()
            return render(request,'base.html')
            # return HttpResponse("data successfully transmited")
        except Exception as e:
            return JsonResponse({'error': str(e)})
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'})
    

# def predict_water_supply(request):
#     if request.method == 'POST':
#         # Retrieve input values from the request
#         Plant = request.POST['Plant']
#         Weather = request.POST['Weather']
#         Temperature_max = float(request.POST['Temperature_max'])
#         Soil = request.POST['Soil']
#         Region = request.POST['Region']
#         Temperature_min = float(request.POST['Temperature_min'])

#         # Load the model and encoders
#         model_and_encoders = joblib.load(r"C:\Users\SIRI VENKAT\Downloads\siri.pkl")

#         # Extract the model and encoders
#         model = model_and_encoders['LinearRegression']
#         crop_type_encoder = model_and_encoders['crop_type_encoder']
#         soil_type_encoder = model_and_encoders['soil_type_encoder']
#         region_encoder = model_and_encoders['region_encoder']
#         weather_condition_encoder = model_and_encoders['weather_condition_encoder']

#         # Convert categorical values to numerical using the label encoders
#         crop_type_encoded = crop_type_encoder.transform([Plant])[0]
#         soil_type_encoded = soil_type_encoder.transform([Soil])[0]
#         region_encoded = region_encoder.transform([Region])[0]
#         weather_condition_encoded = weather_condition_encoder.transform([Weather])[0]

#         # Prepare input data
#         input_data = pd.DataFrame({
#             'CROP TYPE': [crop_type_encoded],
#             'SOIL TYPE': [soil_type_encoded],
#             'REGION': [region_encoded],
#             'WEATHER CONDITION': [weather_condition_encoded],
#             'TEMP_MIN': [Temperature_min],
#             'TEMP_MAX': [Temperature_max]
#         })

#         # Predict water requirement
#         predicted_water_supply = model.predict(input_data)[0]
#         prediction = {
#             'prediction': predicted_water_supply,
#         }

#         # Pass the predicted value to the template
#         return render(request, 'machinelearning.html', context=prediction)
#     else:
#         return render(request, 'machinelearning.html')

temp=False
def predict_water_supply(request):
    if request.method=='POST':
        try:
        # Example input values for temperature and humidity
            Plant = request.POST['Plant']
            Weather = request.POST['Weather']
            Temperature_max = request.POST['Temperature_max']
            Soil = request.POST['Soil']
            Region = request.POST['Region']
            Temperature_min = request.POST['Temperature_min']

            # Create a new DataFrame with the input values
            new_data = pd.DataFrame([[ Plant,Soil,Region,Weather,Temperature_min,Temperature_max ]], columns=['CROP TYPE','SOIL TYPE' ,'REGION','WEATHER CONDITION','TEMP_MIN','TEMP_MAX'])

            # Load the model
            with open(r"C:\Users\SIRI VENKAT\Downloads\linear_regression_model numerical pkl file.pkl", 'rb') as f:
                model = pickle.load(f)

            # Use the model to predict the water supply
            predicted_water_supply = model.predict(new_data)[0]
            predicted_water_supply=abs(((predicted_water_supply*100)-1023))
            predicted_water_supply=int(predicted_water_supply*100/1023)
            prediction={
                'prediction':predicted_water_supply,
            }
            if data11:
                data11.pop()  
            data11.append(predicted_water_supply)
            # Pass the predicted value to the template
            return render(request,'machinelearning.html',context=prediction)
        # except Exception as e:
        #     return JsonResponse({"request":"Fill all sections completely",'error': str(e)})
        except:
            temp=True
            errors={
                'error_message':"FILL ALL SECTIONS"
            }
            return render(request,'machinelearning.html',context=errors)

    else:
        # return HttpResponse(data11)
        print(data11)
        return HttpResponse(data11)
    
def api(request):
    motor_control_value = 1  # Example motor control value

    # You can format the data as JSON
    data = {
        'motor_control_value': motor_control_value
    }

    # Send the data as a JSON response with safe=False
    return JsonResponse(data, safe=False)
