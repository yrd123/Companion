from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from .models import Doctor, Disease
import numpy as np
import pandas as pd
import folium
import geocoder
import geopy
# import ./files

# Create your views here.

def index(request):
    # import pandas as pd
    # df = pd.read_excel("./files/doctor.xlsx")
    # print(df.head())
    # for i in range(len(df)):
    #     print(df.iloc[i, 1])
    #     Doctor.objects.create(name=df.iloc[i, 0],
    #                             address=df.iloc[i, 1],
    #                             latitude=df.iloc[i, 2],
    #                             longitude=df.iloc[i, 3],
    #                             speciality=df.iloc[i, 4]
    #                             )

        # 0 name address latitude logitutde speciality
    return render(request,'index.html')

def predict_disease(request):
    l1=['back_pain','constipation','abdominal_pain','diarrhoea','mild_fever','yellow_urine',
        'yellowing_of_eyes','acute_liver_failure','fluid_overload','swelling_of_stomach',
        'swelled_lymph_nodes','malaise','blurred_and_distorted_vision','phlegm','throat_irritation',
        'redness_of_eyes','sinus_pressure','runny_nose','congestion','chest_pain','weakness_in_limbs',
        'fast_heart_rate','pain_during_bowel_movements','pain_in_anal_region','bloody_stool',
        'irritation_in_anus','neck_pain','dizziness','cramps','bruising','obesity','swollen_legs',
        'swollen_blood_vessels','puffy_face_and_eyes','enlarged_thyroid','brittle_nails',
        'swollen_extremeties','excessive_hunger','extra_marital_contacts','drying_and_tingling_lips',
        'slurred_speech','knee_pain','hip_joint_pain','muscle_weakness','stiff_neck','swelling_joints',
        'movement_stiffness','spinning_movements','loss_of_balance','unsteadiness',
        'weakness_of_one_body_side','loss_of_smell','bladder_discomfort','foul_smell_of urine',
        'continuous_feel_of_urine','passage_of_gases','internal_itching','toxic_look_(typhos)',
        'depression','irritability','muscle_pain','altered_sensorium','red_spots_over_body','belly_pain',
        'abnormal_menstruation','dischromic _patches','watering_from_eyes','increased_appetite','polyuria','family_history','mucoid_sputum',
        'rusty_sputum','lack_of_concentration','visual_disturbances','receiving_blood_transfusion',
        'receiving_unsterile_injections','coma','stomach_bleeding','distention_of_abdomen',
        'history_of_alcohol_consumption','fluid_overload','blood_in_sputum','prominent_veins_on_calf',
        'palpitations','painful_walking','pus_filled_pimples','blackheads','scurring','skin_peeling',
        'silver_like_dusting','small_dents_in_nails','inflammatory_nails','blister','red_sore_around_nose',
        'yellow_crust_ooze']
    if(request.method == 'POST'):
        symptom1 = request.POST["symptom1"]
        symptom2 = request.POST["symptom2"]
        symptom3 = request.POST["symptom3"]
        symptom4 = request.POST["symptom4"]
        symptom5 = request.POST["symptom5"]
        print(symptom1+symptom2+symptom3+symptom4+symptom5)
        disease=['Fungal infection','Allergy','GERD','Chronic cholestasis','Drug Reaction',
        'Peptic ulcer diseae','AIDS','Diabetes','Gastroenteritis','Bronchial Asthma','Hypertension',
        ' Migraine','Cervical spondylosis',
        'Paralysis (brain hemorrhage)','Jaundice','Malaria','Chicken pox','Dengue','Typhoid','hepatitis A',
        'Hepatitis B','Hepatitis C','Hepatitis D','Hepatitis E','Alcoholic hepatitis','Tuberculosis',
        'Common Cold','Pneumonia','Dimorphic hemmorhoids(piles)',
        'Heartattack','Varicoseveins','Hypothyroidism','Hyperthyroidism','Hypoglycemia','Osteoarthristis',
        'Arthritis','(vertigo) Paroymsal  Positional Vertigo','Acne','Urinary tract infection','Psoriasis',
        'Impetigo']

        l2=[0]*len(l1)
        print(l2)
        df=pd.read_csv("./files/Training.csv")
        print(df)
        df.replace({'prognosis':{'Fungal infection':0,'Allergy':1,'GERD':2,'Chronic cholestasis':3,'Drug Reaction':4,
        'Peptic ulcer diseae':5,'AIDS':6,'Diabetes ':7,'Gastroenteritis':8,'Bronchial Asthma':9,'Hypertension ':10,
        'Migraine':11,'Cervical spondylosis':12,
        'Paralysis (brain hemorrhage)':13,'Jaundice':14,'Malaria':15,'Chicken pox':16,'Dengue':17,'Typhoid':18,'hepatitis A':19,
        'Hepatitis B':20,'Hepatitis C':21,'Hepatitis D':22,'Hepatitis E':23,'Alcoholic hepatitis':24,'Tuberculosis':25,
        'Common Cold':26,'Pneumonia':27,'Dimorphic hemmorhoids(piles)':28,'Heart attack':29,'Varicose veins':30,'Hypothyroidism':31,
        'Hyperthyroidism':32,'Hypoglycemia':33,'Osteoarthristis':34,'Arthritis':35,
        '(vertigo) Paroymsal  Positional Vertigo':36,'Acne':37,'Urinary tract infection':38,'Psoriasis':39,
        'Impetigo':40}},inplace=True)
        X= df[l1]
        y = df[["prognosis"]]
        np.ravel(y)

        # TRAINING DATA tr --------------------------------------------------------------------------------
        tr=pd.read_csv("./files/Testing.csv")
        tr.replace({'prognosis':{'Fungal infection':0,'Allergy':1,'GERD':2,'Chronic cholestasis':3,'Drug Reaction':4,
        'Peptic ulcer diseae':5,'AIDS':6,'Diabetes ':7,'Gastroenteritis':8,'Bronchial Asthma':9,'Hypertension ':10,
        'Migraine':11,'Cervical spondylosis':12,
        'Paralysis (brain hemorrhage)':13,'Jaundice':14,'Malaria':15,'Chicken pox':16,'Dengue':17,'Typhoid':18,'hepatitis A':19,
        'Hepatitis B':20,'Hepatitis C':21,'Hepatitis D':22,'Hepatitis E':23,'Alcoholic hepatitis':24,'Tuberculosis':25,
        'Common Cold':26,'Pneumonia':27,'Dimorphic hemmorhoids(piles)':28,'Heart attack':29,'Varicose veins':30,'Hypothyroidism':31,
        'Hyperthyroidism':32,'Hypoglycemia':33,'Osteoarthristis':34,'Arthritis':35,
        '(vertigo) Paroymsal  Positional Vertigo':36,'Acne':37,'Urinary tract infection':38,'Psoriasis':39,
        'Impetigo':40}},inplace=True)

        X_test= tr[l1]
        y_test = tr[["prognosis"]]
        np.ravel(y_test)
        # ------------------------------------------------------------------------------------------------------
        def NaiveBayes():
            from sklearn.naive_bayes import GaussianNB
            gnb = GaussianNB()
            gnb=gnb.fit(X,np.ravel(y))

            # calculating accuracy-------------------------------------------------------------------
            from sklearn.metrics import accuracy_score
            y_pred=gnb.predict(X_test)
            print(accuracy_score(y_test, y_pred))
            print(accuracy_score(y_test, y_pred,normalize=False))
            # -----------------------------------------------------

            psymptoms = [symptom1,symptom2,symptom3,symptom4,symptom5]
            print("i am in")
            print(psymptoms)
            for k in range(0,len(l1)):
                for z in psymptoms:
                    if(z==l1[k]):
                        l2[k]=1

            inputtest = [l2]
            predict = gnb.predict(inputtest)
            predicted=predict[0]
            print("Predicted")
            print(predicted)
            h='no'
            for a in range(0,len(disease)):
                if(predicted == a):
                    h='yes'
                    break
            if (h=='yes'):
                print(disease[a])
                return disease[a]
            else:
                return "Not Found"
            
        predicted_disease = NaiveBayes()
        context = {'predicted_disease': predicted_disease}
        return render(request,'output.html',context)
    return render(request, "symptomsForm.html",{'symptoms':l1})
        

def map_display(request,disease):
    speciality_obj=Disease.objects.filter(disease_name=disease)
    g = geocoder.ip('me')
    lat = g.latlng[0]
    long_ =  g.latlng[1]
    pointA = (lat, long_)
    m = folium.Map(width=800, height=500, location = pointA, zoom_start=8)
    folium.Marker([lat, long_], tooltip="ME", popup="Your address",icon=folium.Icon(color='red')).add_to(m)
    print(speciality_obj)
    if(speciality_obj.exists()):
        
        speciality_obj=speciality_obj.get(disease_name=disease)
        print(speciality_obj)
        doctor_obj=Doctor.objects.filter(speciality=speciality_obj.speciality)
        if(doctor_obj.exists()):
            
            for doctor in doctor_obj:
                # g = geocoder.ip('me')
                # print(g.latlng)
                lat = doctor.latitude
                long_ =  doctor.longitude
                pointA = (lat, long_)
                print(doctor.name)
                # initial folium map
                # m = folium.Map(width=800, height=500, location = pointA, zoom_start=8)
                # location marker
                popup = folium.Popup("<h6>"+doctor.name+"</h6><b>Address:  </b>"+doctor.address,
                     min_width=300,
                     max_width=300)
                folium.Marker([lat, long_], tooltip=doctor.name, popup=popup,icon=folium.Icon(color='black')).add_to(m)
    m = m._repr_html_()
    return render(request, 'maps.html', {'map': m})

@login_required(login_url="admin:login")
def doctor_add(request):

    if request.method == "POST":

        name = request.POST["name"]

        address = request.POST["address"]

        speciality = request.POST["speciality"]

        locator = geopy.Nominatim(user_agent='myGeocoder')

        location = locator.geocode(address)

        lat = location.latitude

        long_ =  location.longitude

        doc_obj = Doctor.objects.create(name = name, address = address, speciality = speciality, latitude=lat, longitude=long_)

        doc_obj.save()

        return redirect("index")
    return render(request,template_name="doctor_add.html")

