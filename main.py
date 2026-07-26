import csv

with open("patients.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow([
        "Patient ID",
        "Name",
        "Age",
        "Gender",
        "Phone",
        "Blood Group",
        "Disease",
        "Admission Date"
    ])
    
def add_patient():
     try:
      patient_id=int(input("ENTER PATIENT ID: "))
      patient_name=input("ENTER PATIENT NAME: ")
      patient_age=int(input("ENTER PATIENT AGE: "))
      patient_gender=input("ENTER PATIENT GENDER: ")
      patient_phone=input("ENTER PATIENT PHONE NUMBER: ")
      patient_blood=input("ENTER PATIENT BLOOD GROUP: ")
      patient_disease=input("ENTER PATIENT DISEASE: ")
      patient_admission_date=input("ENTER PATIENT ADMISSION DATE: ")
     except ValueError:
         print("ENTER A VALID VALUE IN REQUIRED SECTION")
         return
        
     with open("patients.csv","a",newline="") as file:
        writer=csv.writer(file)
        writer.writerow([
            patient_id,
            patient_name,
            patient_age,
            patient_gender,
            patient_phone,
            patient_blood,
            patient_disease,
            patient_admission_date
        ])
            
        
        
     
     