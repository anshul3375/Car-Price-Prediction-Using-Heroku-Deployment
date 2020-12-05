# Importing essential libraries
from flask import Flask, render_template, request
import pickle
import numpy as np

# Load the Random Forest CLassifier model
filename = 'car_price_prediction_model1.pkl'
regressor = pickle.load(open(filename, 'rb'))

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    brand_array = list()
    fuel_array = list()
    transmission_array = list()
    seller_array = list()
    owner_array = list()
    car_array = list()
    
    if request.method == 'POST':
        
        car_brand = request.form['car-brand']
        if car_brand == 'name_Maruti':
            brand_array = brand_array + [1,0,0,0,0,0,0]
        elif car_brand == 'name_Hyundai':
            brand_array = brand_array + [0,1,0,0,0,0,0]
        elif car_brand == 'name_Mahindra':
            brand_array = brand_array + [0,0,1,0,0,0,0]
        elif car_brand == 'name_Tata':
            brand_array = brand_array + [0,0,0,1,0,0,0]
        elif car_brand == 'name_Honda':
            brand_array = brand_array + [0,0,0,0,1,0,0]
        elif car_brand == 'name_Ford':
            brand_array = brand_array + [0,0,0,0,0,1,0]
        elif car_brand == 'name_Toyota':
            brand_array = brand_array + [0,0,0,0,0,0,1]
                    
         
            
        fuel_type = request.form['fuel-type']
        if fuel_type == 'fuel_Diesel':
            fuel_array = fuel_array + [1,0]
        elif fuel_type == 'fuel_Petrol':
            fuel_array = fuel_array + [0,1]
            
            
        transmission_type = request.form['transmission-type']
        if transmission_type == 'transmission_Automatic':
            transmission_array = transmission_array + [1,0]
        elif transmission_type == 'transmission_Manual':
            transmission_array = transmission_array + [0,1]
            
            
        seller_type = request.form['seller-type']
        if seller_type == 'seller_type_Dealer':
            seller_array = seller_array + [1,0]
        elif seller_type == 'seller_type_Individual':
            seller_array = seller_array + [0,1]
            
            
        owner_type = request.form['owner-type']
        if owner_type == 'owner_First Owner':
            owner_array = owner_array + [1,0,0]
        elif owner_type == 'owner_Second Owner':
            owner_array = owner_array + [0,1,0]
        elif owner_type == 'owner_Third Owner':
            owner_array = owner_array + [0,0,1]
    
            
        year = int(request.form['year'])
        km_driven = int(request.form['km_driven'])

        
        car_array = brand_array + fuel_array + transmission_array + seller_array + owner_array + [year, km_driven]
        
        data = np.array([car_array])
        my_prediction = int(regressor.predict(data)[0])
              
        return render_template('result.html', price = my_prediction)



if __name__ == '__main__':
	app.run(debug=True)
