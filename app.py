import flask
import pandas as pd
import numpy as np
from flask import Flask, jsonify, request
import matplotlib.pyplot as plt
import pickle
from sklearn.preprocessing import MinMaxScaler
from flask import request, render_template,send_file,Response,jsonify

from flask_cors import CORS, cross_origin


app = flask.Flask(__name__)
app.config["DEBUG"] = True
CORS(app, support_credentials=True)

@app.route('/check', methods=['GET', 'POST'])
def check():
    return "OK"


@app.route('/predict', methods=['GET', 'POST'])
@cross_origin(supports_credentials=True)
def home():
    ar = [[12000, 60, 19.69, 315.87, 63996.00, 20.81, 1999,  6.00, 0, 22226.00, 99.20, 38.00, 1.00, 0.00, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] , 
     [40000, 60, 30.99, 1533.81, 600.00, 0.00, 1944.00,  1.00, 0.00, 0.00, 0.00, 2.00, 0.00, 0.00, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0] ,
     [500, 36, 5.32, 16.08, 7446395.00, 1622.00, 2013.00,  90.00, 1.00, 1298783.00, 123.20, 151.00, 1.00, 1.00, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1]]

    #json read
    loan_Amount = request.json['loan_Amount']
    ar[0][0] = float(loan_Amount)

    term = request.json['term']
    ar[0][1] = float(term)

    int_rate = request.json['int_rate']
    ar[0][2] = float(int_rate)

    installment = request.json['installment']
    ar[0][3] = float(installment)
    
    annual_inc = request.json['annual_inc']
    ar[0][4] = float(annual_inc)
    
    dti = request.json['dti']
    ar[0][5] = float(dti)

    earliest_cr_line = request.json['earliest_cr_line']
    ar[0][6] = float(earliest_cr_line)

    open_acc = request.json['open_acc']
    ar[0][7] = float(open_acc)

    pub_rec = request.json['pub_rec']
    ar[0][8] = float(pub_rec)

    revol_bal = request.json['revol_bal']
    ar[0][9] = float(revol_bal)

    revol_util = request.json['revol_util']
    ar[0][10] = float(revol_util)

    total_acc = request.json['total_acc']
    ar[0][11] = float(total_acc)

    mort_acc = request.json['mort_acc']
    ar[0][12] = float(mort_acc)

    pub_rec_bankruptcies = request.json['pub_rec_bankruptcies']
    ar[0][13] = float(pub_rec_bankruptcies)

    #ZIP -9 HOME OWNE - 3 APPLICATION TYPE - 2 OTHER - 1 PURPOSE 10
    sub_grade = request.json['sub_grade']
    if sub_grade == 'A2':
        ar[0][14] = float(1);
    elif sub_grade == 'A3':
        ar[0][15] = float(1);
    elif sub_grade == 'A4':
        ar[0][16] = float(1);
    elif sub_grade == 'A5':
        ar[0][17] = float(1);
    elif sub_grade == 'B1':
        ar[0][18] = float(1);
    elif sub_grade == 'B2':
        ar[0][19] = float(1);
    elif sub_grade == 'B3':
        ar[0][20] = float(1);
    elif sub_grade == 'B4':
        ar[0][21] = float(1);
    elif sub_grade == 'B5':
        ar[0][22] = float(1);
    elif sub_grade == 'C1':
        ar[0][23] = float(1);
    elif sub_grade == 'C2':
        ar[0][24] = float(1);
    elif sub_grade == 'C3':
        ar[0][25] = float(1);
    elif sub_grade == 'C4':
        ar[0][26] = float(1);
    elif sub_grade == 'C5':
        ar[0][27] = float(1);
    elif sub_grade == 'D1':
        ar[0][28] = float(1);
    elif sub_grade == 'D2':
        ar[0][29] = float(1);
    elif sub_grade == 'D3':
        ar[0][30] = float(1);
    elif sub_grade == 'D4':
        ar[0][31] = float(1);
    elif sub_grade == 'D5':
        ar[0][32] = float(1);
    elif sub_grade == 'E1':
        ar[0][33] = float(1);
    elif sub_grade == 'E2':
        ar[0][34] = float(1);
    elif sub_grade == 'E3':
        ar[0][35] = float(1);
    elif sub_grade == 'E4':
        ar[0][36] = float(1);
    elif sub_grade == 'E5':
        ar[0][37] = float(1);
    elif sub_grade == 'F1':
        ar[0][38] = float(1);
    elif sub_grade == 'F2':
        ar[0][39] = float(1);
    elif sub_grade == 'F3':
        ar[0][40] = float(1);
    elif sub_grade == 'F4':
        ar[0][41] = float(1);
    elif sub_grade == 'F5':
        ar[0][42] = float(1);
    elif sub_grade == 'G1':
        ar[0][43] = float(1);
    elif sub_grade == 'G2':
        ar[0][44] = float(1);
    elif sub_grade == 'G3':
        ar[0][45] = float(1);
    elif sub_grade == 'G4':
        ar[0][46] = float(1);
    elif sub_grade == 'G5':
        ar[0][47] = float(1);


    purpose = request.json['purpose']
    if purpose == 'credit_card':
        ar[0][50] = float(1);
    elif purpose == 'debt_consolidation':
        ar[0][51] = float(1);
    elif purpose == 'educational':
        ar[0][52] = float(1);
    elif purpose == 'home_improvement':
        ar[0][53] = float(1);
    elif purpose == 'house':
        ar[0][54] = float(1);
    elif purpose == 'major_purchase':
        ar[0][55] = float(1);
    elif purpose == 'medical':
        ar[0][56] = float(1);
    elif purpose == 'moving':
        ar[0][57] = float(1);
    elif purpose == 'other':
        ar[0][58] = float(1);
    elif purpose == 'renewable_energy':
        ar[0][59] = float(1);
    elif purpose == 'small_business':
        ar[0][60] = float(1);
    elif purpose == 'vacation':
        ar[0][61] = float(1);
    elif purpose == 'wedding':
        ar[0][62] = float(1);
    

    
    application_type = request.json['application_type']
    if application_type == 'INDIVIDUAL':
         ar[0][64] = float(1);
    elif application_type == 'JOINT':
         ar[0][65] = float(1);


    home_ownership = request.json['home_ownership']
    if home_ownership == 'OTHER':
         ar[0][66] = float(1);
    elif home_ownership == 'OWN':
         ar[0][67] = float(1);
    elif home_ownership == 'RENT':
         ar[0][68] = float(1);
    

    zipcode = request.json['zipcode']
    if zipcode == '05113':
        ar[0][69] = float(1);
    elif zipcode == '11650':
        ar[0][70] = float(1);
    elif zipcode == '22690':
        ar[0][71] = float(1);
    elif zipcode == '29597':
        ar[0][72] = float(1);
    elif zipcode == '30723':
        ar[0][73] = float(1);
    elif zipcode == '48052':
        ar[0][74] = float(1);
    elif zipcode == '70466':
        ar[0][75] = float(1);
    elif zipcode == '86630':
        ar[0][76] = float(1);
    elif zipcode == '93700':
        ar[0][77] = float(1);
    




    scaler = MinMaxScaler()
    X_test = scaler.fit_transform(ar)
    Pkl_Filename = "Pickle_RL_Model.pkl" 
    with open(Pkl_Filename, 'rb') as file:  
        Pickled_LR_Model = pickle.load(file)
    model_output=Pickled_LR_Model.predict(np.array(X_test))
    var = "Loan status -> " + str (model_output[0])
    #return var
    return var

app.run()
