import csv

# setup
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
 
# add patient function   
def add_patient():
     try:
      patient_id=int(input("ENTER PATIENT ID: "))
      patient_name=input("ENTER PATIENT NAME: ").title()
      patient_age=int(input("ENTER PATIENT AGE: "))
      patient_gender=input("ENTER PATIENT GENDER: ").upper()
      patient_phone=input("ENTER PATIENT PHONE NUMBER: ")
      patient_blood=input("ENTER PATIENT BLOOD GROUP: ").upper()
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
        print("PATIENT ADDED SUCCESSFULLY")
        
# view patients function
def view_patients():
    found=False
    with open("patients.csv","r") as file:
        reader=csv.reader(file)
        next(reader)
        print("="*35)
        print("    REGISTERED PATIENTS")
        for patient in reader:
            found=True
            print("="*35) 
            print(f"PATIENT_ID: {patient[0]}")
            print(f"PATIENT_NAME: {patient[1]}")
            print(f"PATIENT_AGE: {patient[2]}")
            print(f"PATIENT_GENDER: {patient[3]}")
            print(f"PATIENT_PHONENO.: {patient[4]}")
            print(f"PATIENT_BLOODGROUP: {patient[5]}")
            print(f"PATIENT_DISEASE: {patient[6]}")
            print(f"PATIENT_ADMISSION_DATE: {patient[7]}")
            print("="*35)
            
        if not found:
            print("NO REGISTERED PATIENTS AT THE MOMENT ")

# search patient
def search_patient():
    try:
       found=False
       patient_id=int(input("ENTER PATIENT ID: "))
       with open("patients.csv","r") as file:
           reader=csv.reader(file)
           next(reader)
           for patient in reader:
               if int(patient[0])==patient_id:
                    found=True
                    print("="*35) 
                    print(f"PATIENT_ID: {patient[0]}")
                    print(f"PATIENT_NAME: {patient[1]}")
                    print(f"PATIENT_AGE: {patient[2]}")
                    print(f"PATIENT_GENDER: {patient[3]}")
                    print(f"PATIENT_PHONENO.: {patient[4]}")
                    print(f"PATIENT_BLOODGROUP: {patient[5]}")
                    print(f"PATIENT_DISEASE: {patient[6]}")
                    print(f"PATIENT_ADMISSION_DATE: {patient[7]}")
                    print("="*35)
                    break
           if not found:
              print("PATIENT NOT FOUND")
              return
    except ValueError:
        print("ENTER A VALID PATIENT ID")
        return

                   
       

            

        
        
            
        
        
     
     