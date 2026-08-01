import csv

def choice():
    
 while True:
    print("=" * 35)
    print(" HOSPITAL MANAGEMENT SYSTEM ")
    print("=" * 35)
    print("1) PATIENT MANAGEMENT")
    print("2) DOCTOR MANAGEMENT")
    print("3) APPOINTMENT MANAGEMENT")
    print("4) BILLING MANAGEMENT")
    print("5) HOSPITAL STATISTICS")
    print("6) EXIT")
    print("=" * 35)

    try:
        choice=int(input("ENTER YOUR CHOICE(1-6): "))

        if choice==1:
            while True:
                print("=" * 35)
                print("    PATIENT MANAGEMENT")
                print("=" * 35)
                print("1) ADD PATIENT")
                print("2) VIEW PATIENTS")
                print("3) SEARCH PATIENT")
                print("4) UPDATE PATIENT")
                print("5) DELETE PATIENT")
                print("6) BACK")
                print("=" * 35)

                try:
                    patient_choice=int(input("ENTER YOUR CHOICE(1-6): "))

                    if patient_choice==1:
                        add_patient()

                    elif patient_choice==2:
                        view_patients()

                    elif patient_choice==3:
                        search_patient()

                    elif patient_choice==4:
                        update_patient()

                    elif patient_choice==5:
                        delete_patient()

                    elif patient_choice==6:
                        break

                    else:
                        print("ENTER A CHOICE BETWEEN(1-6)")

                except ValueError:
                    print("ENTER A VALID VALUE")
                    
        elif choice==2:
            while True:
                print("=" * 35)
                print("    DOCTOR MANAGEMENT")
                print("=" * 35)
                print("1) ADD DOCTOR")
                print("2) VIEW DOCTORS")
                print("3) SEARCH DOCTOR")
                print("4) UPDATE DOCTOR")
                print("5) DELETE DOCTOR")
                print("6) BACK")
                print("=" * 35)

                try:
                    doctor_choice=int(input("ENTER YOUR CHOICE(1-6): "))

                    if doctor_choice==1:
                        add_doctor()

                    elif doctor_choice==2:
                        view_doctors()

                    elif doctor_choice==3:
                        search_doctor()

                    elif doctor_choice==4:
                        update_doctor()

                    elif doctor_choice==5:
                        delete_doctor()

                    elif doctor_choice==6:
                        break

                    else:
                        print("ENTER A CHOICE BETWEEN(1-6)")

                except ValueError:
                    print("ENTER A VALID VALUE")

        elif choice==3:
            while True:
                print("=" * 35)
                print("  APPOINTMENT MANAGEMENT")
                print("=" * 35)
                print("1) ADD APPOINTMENT")
                print("2) VIEW APPOINTMENTS")
                print("3) SEARCH APPOINTMENT")
                print("4) UPDATE APPOINTMENT")
                print("5) DELETE APPOINTMENT")
                print("6) BACK")
                print("=" * 35)

                try:
                    appointment_choice=int(input("ENTER YOUR CHOICE(1-6): "))

                    if appointment_choice==1:
                        add_appointment()

                    elif appointment_choice==2:
                        view_appointments()

                    elif appointment_choice==3:
                        search_appointment()

                    elif appointment_choice==4:
                        update_appointment()

                    elif appointment_choice==5:
                        delete_appointment()

                    elif appointment_choice==6:
                        break

                    else:
                        print("ENTER A CHOICE BETWEEN(1-6)")

                except ValueError:
                    print("ENTER A VALID VALUE")

        elif choice==4:
            while True:
                print("=" * 35)
                print("    BILLING MANAGEMENT")
                print("=" * 35)
                print("1) ADD BILL")
                print("2) VIEW BILLS")
                print("3) SEARCH BILL")
                print("4) DELETE BILL")
                print("5) BACK")
                print("=" * 35)

                try:
                    bill_choice=int(input("ENTER YOUR CHOICE(1-5): "))

                    if bill_choice==1:
                        add_bill()

                    elif bill_choice==2:
                        view_bills()

                    elif bill_choice==3:
                        search_bill()

                    elif bill_choice==4:
                        delete_bill()

                    elif bill_choice==5:
                        break

                    else:
                        print("ENTER A CHOICE BETWEEN(1-5)")

                except ValueError:
                    print("ENTER A VALID VALUE")

        elif choice==5:
            statistics()

        elif choice==6:
            print("=" * 35)
            print("THANK YOU FOR USING")
            print("HOSPITAL MANAGEMENT SYSTEM")
            print("=" * 35)
            break

        else:
            print("ENTER A CHOICE BETWEEN(1-6)")

    except ValueError:
        print("ENTER A VALID VALUE")

# patients setup
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
      patient_disease=input("ENTER PATIENT DISEASE: ").title()
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
            return

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
                    print("PATIENT FOUND")
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

# update patient
def update_patient():
    try:
        found=False
        patient_id=int(input("ENTER PATIENT ID TO UPDATE: "))
        with open("patients.csv","r") as file:
            reader=csv.reader(file)
            next(reader)
            patients=list(reader)
            for patient in patients:
                if int(patient[0])==patient_id:
                    found=True
                    print("="*35)
                    print("PATIENT FOUND")
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
    while True:
        print("="*35)
        print("    WHAT YOU WANT TO UPDATE?: ")
        print("="*35)
        print("1) NAME")
        print("2) AGE")
        print("3) GENDER")
        print("4) PHONE")
        print("5) BLOOD GROUP")
        print("6) DISEASE")
        print("7) ADMISSION DATE")
        print("8) CANCEL")
        print("="*35)
        try:
         choice=int(input("ENTER YOUR CHOICE(1-8): "))
         if choice==1:
            try:
                new_name=input("ENTER PATIENT'S NEW NAME: ")
                patient[1]=new_name
                print("NAME UPDATED SUCCESSFULLY")
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
            except ValueError:
                print("ENTER A VALID PATIENT NAME")
                return     
         elif choice==2:
            try:
                new_age=int(input("ENTER PATIENT'S NEW AGE: "))
                patient[2]=new_age
                print("AGE UPDATED SUCCESSFULLY")
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
            except ValueError:
                print("ENTER A VALID AGE")
                return       
         elif choice==3:
            try:
                new_gender=input("ENTER PATEINT'S NEW GENDER: ").upper()
                patient[3]=new_gender
                print("GENDER UPDATED SUCCESSFULLY")
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
            except ValueError:
                print("ENTER A VALID AGE")
                return       
         elif choice==4:
            try:
                new_phoneno=input("ENTER PATEINT'S NEW PHONE NUMBER: ")
                patient[4]=new_phoneno
                print("PHONE NUMBER UPDATED SUCCESSFULLY")
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
            except ValueError:
                print("ENTER A VALID PHONE NUMBER")
                return                      
         elif choice==5:
            try:
                new_bloodgrp=input("ENTER PATEINT'S NEW BLOODGROUP: ").upper()
                patient[5]=new_bloodgrp
                print("BLOODGROUP UPDATED SUCCESSFULLY")
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
            except ValueError:
                print("ENTER A VALID BLOODGROUP")
                return
         elif choice==6:
            try:
                new_disease=input("ENTER PATEINT'S NEW DISEASE: ").title()
                patient[6]=new_disease
                print("DISEASE UPDATED SUCCESSFULLY")
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
            except ValueError:
                print("ENTER A VALID DISEASE")
                return
         elif choice==7:
            try:
                new_admission_date=input("ENTER PATEINT'S NEW ADMISSIONN DATE: ")
                patient[7]=new_admission_date
                print("ADMISSION DATE UPDATED SUCCESSFULLY")
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
            except ValueError:
                print("ENTER A VALID DATE")
                return
         elif choice==8:
             break
         else:
             print("ENTER A CHOICE BETWEEN (1-8)")
             continue
        
        except ValueError:
            print("ENTER A VALID CHOICE")
            continue
         
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
     for patient in patients:
        writer.writerow(patient)
        
# delete patient function
def delete_patient():
    try:
        found=False
        patient_id=int(input("ENTER PATIENT ID YOU WANT TO DELETE: "))
        with open("patients.csv","r") as file:
                reader=csv.reader(file)
                next(reader)
                patients=list(reader)
                for patient in patients:
                    if int(patient[0])==patient_id:
                        found=True
                        print("="*35)
                        print("PATIENT FOUND")
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
    while True:
        choice=input("ARE YOU SURE YOU WANT TO DELETE THIS PATIENT?(Y/N): ").upper()
        if choice=="Y":
            patients.remove(patient)
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
                for patient in patients:
                    writer.writerow(patient)
                print("PATIENT DELETED SUCCESSFULLY")
                break
        elif choice=="N":
            print("DELETION CANCELLED")
            break
            
        else:
            print("ENTER EXACTLY(Y/N)")
            continue
        
#doctors setup
with open("doctors.csv","w") as file:
    writer=csv.writer(file)
    writer.writerow([
        "Doctor Id",
        "Doctor Name",
        "Doctor Specialization"
    ])
    
# add doctor
def add_doctor():
    try:
        doctor_id=int(input("ENTER DOCTOR ID: "))
        doctor_name=input("ENTER DOCTOR NAME: ")
        doctor_specialization=input("ENTER DOCTOR SPECIALIZATION: ")
    except ValueError:
        print("ENTER A VALID DOCTOR ID")
        return
    with open("doctors.csv","a",newline="") as file:
        writer=csv.writer(file)
        writer.writerow([
            doctor_id,
            doctor_name,
            doctor_specialization
        ])
        print("DOCTOR ADDED SUCCESSFULLY")
        
#search doctor
def search_doctor():
    try:
        found=False
        doctor_id=int(input("ENTER DOCTOR'S ID: "))
        with open("doctors.csv","r") as file:
            reader=csv.reader(file)
            next(reader)
            for doctor in reader:
                if int(doctor[0])==doctor_id:
                    found=True
                    print("="*35)
                    print(f"DOCTOR_ID: {doctor[0]}")
                    print(f"DOCTOR_NAME: {doctor[1]}")
                    print(f"DOCTOR_SPECIALIZATION: {doctor[2]}")
                    print("="*35)
                    break
            if not found:
                print("DOCTOR NOT FOUND")
                return
    except ValueError:
        print("ENTER A VALID DOCTOR ID")
        return
        
# view doctors
def view_doctors():
        found=False
        with open("doctors.csv","r") as file:
            reader=csv.reader(file)
            print("="*35)
            print("    REGISTERED DOCTORS")
            next(reader)
            for doctor in reader:
                found=True
                print("="*35)
                print(f"DOCTOR_ID: {doctor[0]}")
                print(f"DOCTOR_NAME: {doctor[1]}")
                print(f"DOCTOR_SPECIALIZATION: {doctor[2]}")
                print("="*35)
                
            if not found:
                print("NO REGISTERED DOCTORS AT THE MOMENT")
                return
                
# update doctor
def update_doctor():
    try:
        found=False
        doctor_id=int(input("ENTER DOCTOR'S ID TO UPDATE: "))
        with open("doctors.csv","r") as file:
            reader=csv.reader(file)
            next(reader)
            doctors=list(reader)
            for doctor in doctors:
                if int(doctor[0])==doctor_id:
                    found=True
                    print("="*35)
                    print(f"DOCTOR_ID: {doctor[0]}")
                    print(f"DOCTOR_NAME: {doctor[1]}")
                    print(f"DOCTOR_SPECIALIZATION: {doctor[2]}")
                    print("="*35)
                    break
            if not found:
                print("DOCTOR NOT FOUND")
                return
    except ValueError:
        print("ENTER A VALID DOCTOR ID")
        return
        
    while True:
        print("="*35)
        print("    WHAT YOU WANT TO UPDATE")
        print("="*35)
        print("1)DOCTOR_ID")
        print("2) DOCTOR_NAME")
        print("3)DOCTOR_SPECIALIZATION")
        try:
           choice=int(input("ENTER YOUR CHOICE(1-3): "))
           if choice==1:
              new_id=int(input("ENTER DOCTOR'S NEW ID: "))
              doctor[0]=new_id
              print("DOCTOR ID UPDATED SUCCESSFULLY")
              print("="*35)
              print(f"DOCTOR_ID: {doctor[0]}")
              print(f"DOCTOR_NAME: {doctor[1]}")
              print(f"DOCTOR_SPECIALIZATION: {doctor[2]}")
              print("="*35)
              break
           elif choice==2:
               new_name=input("ENTER DOCTOR'S NEW NAME: ")
               doctor[1]=new_name
               print("DOCTOR NAME UPDATED SUCCESSFULLY")
               print("="*35)
               print(f"DOCTOR_ID: {doctor[0]}")
               print(f"DOCTOR_NAME: {doctor[1]}")
               print(f"DOCTOR_SPECIALIZATION: {doctor[2]}")
               print("="*35)
               break
           elif choice==3:
               new_specialization=input("ENTER DOCTOR'S NEW SPECIALIZATION: ")
               doctor[2]=new_specialization
               print("DOCTOR'S SPECIALIZATION UPDATED SUCCESSFULLY")
               print("="*35)
               print(f"DOCTOR_ID: {doctor[0]}")
               print(f"DOCTOR_NAME: {doctor[1]}")
               print(f"DOCTOR_SPECIALIZATION: {doctor[2]}")
               print("="*35)
               break
           else:
               print("ENTER A CHOICE BETWEEN(1-3)ONLY")
               continue
        except ValueError:
            print("ENTER A VALID VALUE")
            continue
    with open("doctors.csv", "w", newline="") as file:
         writer = csv.writer(file)
         writer.writerow([
            "Doctor Id",
            "Doctor Name",
            "Doctor Specialization"
        ])
         for doctor in doctors:
            writer.writerow(doctor)
            
# delete doctor
def delete_doctor():
    try:
        found=False
        doctor_id=int(input("ENTER DOCTOR ID: "))
        with open("doctors.csv","r") as file:
            reader=csv.reader(file)
            next(reader)
            doctors=list(reader)
            for doctor in doctors:
                if int(doctor[0])==doctor_id:
                    found=True
                    print("DOCTOR FOUND")
                    print("="*35)
                    print(f"DOCTOR_ID: {doctor[0]}")
                    print(f"DOCTOR_NAME: {doctor[1]}")
                    print(f"DOCTOR_SPECIALIZATION: {doctor[2]}")
                    print("="*35)
                    break
            if not found:
                print("DOCTOR NOT FOUND")
                return
    except ValueError:
         print("ENTER A VALID DOCTOR ID")
         return
                    
    while True:
        choice=input("ARE YOU SURE YOU WANT TO DLETE THIS DOCTOR?(Y/N)").upper()
        if choice=="Y":
            doctors.remove(doctor)
            with open("doctors.csv", "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow([
                    "Doctor Id",
                    "Doctor Name",
                    "Doctor Specialization"      
                ])
                for doctor in doctors:
                    writer.writerow(doctor)
            print("DOCTOR DELETED SUCCESSFULLY")
            break
        elif choice=="N":
            print("DELETION CANCELLED")
            break
        else:
            print("ENTER EXACTLY (Y/N)")
            continue
         
# appointment setup
with open("appointments.csv","w",newline="") as file:
    writer=csv.writer(file)
    
    writer.writerow([
        "Appointment Id",
        "Patient Id",
        "Doctor Id",
        "Appointment Date",
        "Appointment Time",
        "Appointment Status"
    ])
    
              
# add appointment function
def add_appointment():
    try:
       found_patient=False
       found_doctor=False
       appointment_id=int(input("ENTER APPOINTMENT ID: "))
       with open("appointments.csv","r") as file:
           reader=csv.reader(file)
           next(reader)
           appointments=list(reader)
           for appointment in appointments:
               if int(appointment[0])==appointment_id:
                   print("APPOINTMENT ID ALREADY EXISTS")
                   return
    except ValueError:
       print("ENTER VALID APPOINTMENT")
       return
                   
    try:
          patient_id=int(input("ENTER PATIENT ID: "))
          with open("patients.csv","r") as file:
            reader=csv.reader(file)
            next(reader)
            patients=list(reader)
            for patient in patients:
                if int(patient[0])==patient_id:
                    found_patient=True
                    continue
            if not found_patient:
                print("PATIENT NOT FOUND")
                return
    except ValueError:
           print("ENTER A VALID PATIENT ID")
           return
                
    try:
           doctor_id=int(input("ENTER DOCTOR ID: "))
           with open("doctors.csv","r") as file:
               reader=csv.reader(file)
               next(reader)
               doctors=list(reader)
               for doctor in doctors:
                   if int(doctor[0])==doctor_id:
                       found_doctor=True
                       continue
               if not found_doctor:
                   print("DOCTOR NOT FOUND")
                   return
    except ValueError:
            print("ENTER A VALID DOCTOR ID ")
            return
                    
    appointment_date=input("ENTER APPOINTMENT DATE: ")
    appointment_time=input("ENTER APPOINTMENT TIME: ")
    appointment_status="Scheduled"
    with open("appointments.csv","a",newline="") as file:
        writer=csv.writer(file)
        writer.writerow([
            appointment_id,
            patient_id,
            doctor_id,
            appointment_date,
            appointment_time,
            appointment_status
        ])
        print("APPOINTMENT ADDED SUCCESSFULLY")
        
# view appointments function
def view_appointments():
    found=False
    with open("appointments.csv","r") as file:
        reader=csv.reader(file)
        next(reader)
        print("="*35)
        print("    REGISTERED APPOINTMENTS")
        for appointment in reader:
            found=True
            print("="*35)
            print(f"APPOINTMENT_ID: {appointment[0]}")
            print(f"PATIENT_ID: {appointment[1]}")
            print(f"DOCTOR_ID: {appointment[2]}")
            print(f"APPOINTMENT_DATE: {appointment[3]}")
            print(f"APPOINTMENT_TIME: {appointment[4]}")
            print(f"APPOINTMENT_STATUS: {appointment[5]}")
            print("="*35)
                        
        if not found:
            print("NO REGISTERED APPOINTMENTS AT THE MOMENT")
            return
            
#search appointment function
def search_appointment():
    try:
        found=False
        appointment_id=int(input("ENTER APPOINTMENT ID: "))
        with open("appointments.csv","r") as file:
            reader=csv.reader(file)
            next(reader)
            for appointment in reader:
                if int(appointment[0])==appointment_id:
                    found=True
                    print("="*35)
                    print(f"APPOINTMENT_ID: {appointment[0]}")
                    print(f"PATIENT_ID: {appointment[1]}")
                    print(f"DOCTOR_ID: {appointment[2]}")
                    print(f"APPOINTMENT_DATE: {appointment[3]}")
                    print(f"APPOINTMENT_TIME: {appointment[4]}")
                    print(f"APPOINTMENT_STATUS: {appointment[5]}")
                    print("="*35)
                    break
            if not found:
                print("APPOINTMENT NOT FOUND")
                return
    except ValueError:
        print("ENTER A VALID APPOINTMENT ID")
        return
    
# update appointment function
def update_appointment():
    try:
        found=False
        appointment_id=int(input("ENTER APPOINTMENT ID TO UPDATE: "))
        with open("appointments.csv","r") as file:
            reader=csv.reader(file)
            next(reader)
            appointments=list(reader)
            for appointment in appointments:
                if int(appointment[0])==appointment_id:
                    found=True
                    print("="*35)
                    print(f"APPOINTMENT_ID: {appointment[0]}")
                    print(f"PATIENT_ID: {appointment[1]}")
                    print(f"DOCTOR_ID: {appointment[2]}")
                    print(f"APPOINTMENT_DATE: {appointment[3]}")
                    print(f"APPOINTMENT_TIME: {appointment[4]}")
                    print(f"APPOINTMENT_STATUS: {appointment[5]}")
                    print("="*35)
                    break
            if not found:
                    print("APPOINTMENT NOT FOUND")
                    return
    except ValueError:
            print("ENTER A VALID APPOINTMENT ID")
            return
        
    while True:
            print("="*35)
            print("    WHAT YOU WANT TO UPDATE")
            print("="*35)
            print("1)APPOINTMENT_DATE")
            print("2) APPOINTMENT_TIME")
            print("3)APPOINTMENT_STATUS")
            
            try: 
                choice=int(input("ENTER YOUR CHOICE(1-3): "))
                if choice==1:
                  new_date=input("ENTER NEW APPOINTMENT DATE: ")
                  appointment[3]=new_date
                  print("APPOINTMENT DATE UPDATED SUCCESSFULLY")
                  print(f"APPOINTMENT_ID: {appointment[0]}")
                  print(f"PATIENT_ID: {appointment[1]}")
                  print(f"DOCTOR_ID: {appointment[2]}")
                  print(f"APPOINTMENT_DATE: {appointment[3]}")
                  print(f"APPOINTMENT_TIME: {appointment[4]}")
                  print(f"APPOINTMENT_STATUS: {appointment[5]}")
                  print("="*35)
                  break
                elif choice==2:
                   new_time=input("ENTER NEW APPOINTMENT TIME: ")
                   appointment[4]=new_time
                   print("APPOINTMENT TIME UPDATED SUCCESSFULLY")
                   print(f"APPOINTMENT_ID: {appointment[0]}")
                   print(f"PATIENT_ID: {appointment[1]}")
                   print(f"DOCTOR_ID: {appointment[2]}")
                   print(f"APPOINTMENT_DATE: {appointment[3]}")
                   print(f"APPOINTMENT_TIME: {appointment[4]}")
                   print(f"APPOINTMENT_STATUS: {appointment[5]}")
                   print("="*35)
                   break
                elif choice==3:
                   new_status=input("ENTER NEW APPOINTMENT STATUS: ")
                   appointment[5]=new_status
                   print("APPOINTMENT STATUS UPDATED SUCCESSFULLY")
                   print(f"APPOINTMENT_ID: {appointment[0]}")
                   print(f"PATIENT_ID: {appointment[1]}")
                   print(f"DOCTOR_ID: {appointment[2]}")
                   print(f"APPOINTMENT_DATE: {appointment[3]}")
                   print(f"APPOINTMENT_TIME: {appointment[4]}")
                   print(f"APPOINTMENT_STATUS: {appointment[5]}")
                   print("="*35)
                   break
                else:
                   print("ENTER A CHOICE BETWEEN(1-3)ONLY")
                   continue
            except ValueError:
                print("ENTER A VALID VALUE")
                continue
    with open("appointments.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            "Appointment Id",
            "Patient Id",
            "Doctor Id",
            "Appointment Date",
            "Appointment Time",
            "Appointment Status"   
        ])
        for appointment in appointments:
            writer.writerow(appointment)
            
# delete appointment function
def delete_appointment():
    try:
        found=False
        appointment_id=int(input("ENTER APPOINTMENT ID YOU WANT TO DELETE: "))
        with open("appointments.csv","r") as file:
                reader=csv.reader(file)
                next(reader)
                appointments=list(reader)
                for appointment in appointments:
                    if int(appointment[0])==appointment_id:
                        found=True
                        print(f"APPOINTMENT_ID: {appointment[0]}")
                        print(f"PATIENT_ID: {appointment[1]}")
                        print(f"DOCTOR_ID: {appointment[2]}")
                        print(f"APPOINTMENT_DATE: {appointment[3]}")
                        print(f"APPOINTMENT_TIME: {appointment[4]}")
                        print(f"APPOINTMENT_STATUS: {appointment[5]}")
                        print("="*35)
                        break
                if not found:
                        print("APPOINTMENT NOT FOUND")
                        return
    except ValueError:
            print("ENTER A VALID APPOINTMENT ID")
            return
    while True:
        choice=input("ARE YOU SURE YOU WANT TO DELETE THIS APPOINTMENT?(Y/N): ").upper()
        if choice=="Y":
            appointments.remove(appointment)
            with open("appointments.csv", "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow([
                    "Appointment Id",
                    "Patient Id",
                    "Doctor Id",
                    "Appointment Date",
                    "Appointment Time",
                    "Appointment Status"   
                    ])
                for appointment in appointments:
                    writer.writerow(appointment)
                print("APPOINTMENT DELETED SUCCESSFULLY")
                break
        elif choice=="N":
            print("DELETION CANCELLED")
            break
            
        else:
            print("ENTER EXACTLY(Y/N)")
            continue
        
# billing setup
with open("bills.csv","w") as file:
     writer=csv.writer(file)
     writer.writerow([
         "Bill Id",
         "Patient Id",
         "Doctor Id",
         "Consultation Fee",
         "Medicine Charges",
         "Other Charges",
         "Total Amount"
    ])

# add bill
def add_bill():
    found_patient=False
    found_doctor=False
    try:
        bill_id=int(input("ENTER BILL ID: "))
        with open("bills.csv","r") as file:
            reader=csv.reader(file)
            next(reader)
            bills=list(reader)
            for bill in bills:
                if int(bill[0])==bill_id:
                    print("BILL ALREADY EXISTS")
                    return                   
  
    except ValueError:
        print("ENTER A VALID BILL ID")
        return
    
    try:
        patient_id=int(input("ENTER PATIENT ID: "))
        with open("patients.csv","r") as file:
            reader=csv.reader(file)
            next(reader)
            patients=list(reader)
            for patient in patients:
                if int(patient[0])==patient_id:
                    found_patient=True
                    print("PATIENT FOUND")
            if not found_patient:
                print("PATIENT NOT FOUND")
                return
    except ValueError:
        print(" ENTER A VALID PATIENT ID")
        return
        
    try:
        doctor_id=int(input("ENTER DOCTOR ID: "))
        with open("doctors.csv","r") as file:
            reader=csv.reader(file)
            next(reader)
            doctors=list(reader)
            for doctor in doctors:
                if int(doctor[0])==doctor_id:
                    found_doctor=True
                    print("DOCTOR FOUND")
            if not found_doctor:
                print("DOCTOR NOT FOUND")
                return
    except ValueError:
        print("ENTER A VALID DOCTOR ID")
        return
        
    try:
        consultation_fee=int(input("ENTER CONSULTATION FEE: "))
        medicine_charges=int(input("ENTER MEDICINE CHARGES: "))
        other_charges=int(input("ENTER OTHER CHARGES: "))
        total_fee=consultation_fee+medicine_charges+other_charges
        with open("bills.csv","a",newline="") as file:
            writer=csv.writer(file)
            writer.writerow([
                bill_id,
                patient_id,
                doctor_id,
                consultation_fee,
                medicine_charges,
                other_charges,
                total_fee
            ])
            print("BILL ADDED SUCCESSFULLY")                      
    except ValueError:
            print("ENTER A VALID VALUE IN REQUIRED FIELD")
            return
        
# view bills
def view_bills():
    found=False
    with open("bills.csv","r") as file:
        reader=csv.reader(file)
        next(reader)
        print("="*35)
        print("    REGISTERED BILLS")
        for bill in reader:
            found=True
            print("="*35)
            print(f"BILL_ID: {bill[0]}")
            print(f"PATIENT_ID: {bill[1]}")
            print(f"DOCTOR_ID: {bill[2]}")
            print(f"CONSULTATION_FEE: {bill[3]}")
            print(f"MEDICINE_CHARGES: {bill[4]}")
            print(f"OTHER_CHARGES: {bill[5]}")
            print(f"TOTAL_AMOUNT: {bill[6]}")
            print("="*35)
        if not found:
            print("NO REGISTERED BILLS AT THE MOMENT")
            return
        
# search bill
def search_bill():
    try:
        found=False
        bill_id=int(input("ENTER THE BILL ID: "))
        with open("bills.csv","r") as file:
            reader=csv.reader(file)
            next(reader)
            for bill in reader:
                if int(bill[0])==bill_id:
                    found=True
                    print("="*35)
                    print(f"BILL_ID: {bill[0]}")
                    print(f"PATIENT_ID: {bill[1]}")
                    print(f"DOCTOR_ID: {bill[2]}")
                    print(f"CONSULTATION_FEE: {bill[3]}")
                    print(f"MEDICINE_CHARGES: {bill[4]}")
                    print(f"OTHER_CHARGES: {bill[5]}")
                    print(f"TOTAL_AMOUNT: {bill[6]}")
                    print("="*35)
                    break
            if not found:
                print("BILL NOT FOUND")
                return
    except ValueError:
        print("ENTER A VALID BILL ID")
        return
    
# delete bill
def delete_bill():
    try:
        found=False
        bill_id=int(input("ENTER THE BILL ID: "))
        with open("bills.csv","r") as file:
            reader=csv.reader(file)
            next(reader)
            bills=list(reader)
            for bill in bills:
                if int(bill[0])==bill_id:
                    found=True
                    print("="*35)
                    print(f"BILL_ID: {bill[0]}")
                    print(f"PATIENT_ID: {bill[1]}")
                    print(f"DOCTOR_ID: {bill[2]}")
                    print(f"CONSULTATION_FEE: {bill[3]}")
                    print(f"MEDICINE_CHARGES: {bill[4]}")
                    print(f"OTHER_CHARGES: {bill[5]}")
                    print(f"TOTAL_AMOUNT: {bill[6]}")
                    print("="*35)
                    break
            if not found:
                print("BILL NOT FOUND")
                return
    except ValueError:
        print("ENTER A VALID BILL ID")
        return
    
    while True:
        choice=input("DO YOU REALLY WANT TO DELETE THE BILL?(Y/N): ").upper()
        if choice=="Y":
            bills.remove(bill)
            with open("bills.csv","w",newline="") as file:
                    writer=csv.writer(file)
                    writer.writerow([
                        "Bill Id",
                        "Patient Id",
                        "Doctor Id",
                        "Consultation Fee",
                        "Medicine Charges",
                        "Other Charges",
                        "Total Amount"                       
                    ])
                    for bill in bills:
                        writer.writerow(bill)
            print("BILL DELETED SUCCESSFULLY")
            break
        elif choice=="N":
            print("DELETION CANCELLED")
            break
        else:
            print("ENTER EXACTLY(Y/N)")
            continue
        
#hospital statistics
def statistics():
    with open("patients.csv","r") as file:
        reader=csv.reader(file)
        next(reader)
        total_patients=sum(1 for row in reader)
    with open("doctors.csv","r") as file:
            reader=csv.reader(file)
            next(reader)
            total_doctors=sum(1 for row in reader)
    with open("appointments.csv","r") as file:
            reader=csv.reader(file)
            next(reader)
            total_appointments=sum(1 for row in reader)
    with open("bills.csv","r") as file:
            reader=csv.reader(file)
            next(reader)
            total_bills=sum(1 for row in reader)
            
    print("="*35)
    print("    HOSPITAL STATISTICS")
    print("="*35)
    print(f"TOTAL PATIENTS: {total_patients}")
    print(f"TOTAL DOCTORS: {total_doctors}")
    print(f"TOTAL APPOINTMENTS: {total_appointments}")
    print(f"TOTAL BILLS: {total_bills}")
    print("="*35)
    
choice()
    
    
    

    
        
    
        
            
            
        
                  
            
            
        
    
        
        
                    
        
        
                            
                         
    
    
            
        
        
                    
        
    
    
             

            
            
                    
        
        
            
                       
    
    

    

            
        
        

            

        
        
            
        
        
     
     