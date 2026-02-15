
print("Program Started")
from models import Patient,Doctor,Appontment,MedicalRecord,Bills
from services import HospitalServices,AuthService

def admin_menu():
    while True:
        print("\n--- ADMIN MENU ---")
        print("1.Add Patient")
        print("2.view Patient")
        print("3.Add Dioctor")
        print("4.view Doctor")
        print("5.view Appointments")
        print("6.view Bills")
        print("7.Logout")
        
        choice = input("Enter Choice:")
        
        if choice == "1":
            name = input("Name: ")
            age = int(input("age: "))
            gender = input("gender: ")
            phone = int(input("phone: "))
            address = input("address: ")
            HospitalServices.add_patient(Patient(name,age,gender,phone,address))
            
        elif choice == "2":
            HospitalServices.view_patient()
            
        elif choice == "3":
            name = input("Name: ")
            phone = input("phone: ")
            specilization = input("specilization: ")
            department = input("department: ")
            salary = input("salary:")
            HospitalServices.add_doctor(Doctor(name,phone,specilization,department,salary))
            
            
        elif choice == "4":
            HospitalServices.view_doctor()
            
        elif choice == "5":
            HospitalServices.view_appointment()
            
        elif choice == "6":
            HospitalServices.view_bill()
            
        elif choice == "7":
            break
        
        else:
            print("choose correct option----")
            
            
def reception_menu():
    while True:
        print("\n ----- RECEPTION MENU -------")
        print("1. Add patient")
        print("2. Book Appointment")
        print("3.view bills")
        print("4. Logout")
        
        choice = input("enter your choice: ")
        
        if choice == "1":
            name = input("Name: ")
            age = int(input("age: "))
            gender = input("gender: ")
            phone = int(input("phone: "))
            address = input("address: ")
            HospitalServices.add_patient(Patient(name,age,gender,phone,address))
            
        elif choice == "2":
            doctor_id = int(input("Doctor Id: "))
            patient_id = int(input("patient_id"))
            appointment_date = input("Appointment_date(YYYY-MM-DD)")
            status = input("status :")
            HospitalServices.book_appointment(Appontment(doctor_id,patient_id,appointment_date,status))
            
        elif choice == "3":
            HospitalServices.view_bill()
            
            
        elif choice == "4":
            break
        
        else:
            print("enter correct choice----")
            
            
            
def doctor_menu():
    while True:
        print("\n ---------DOCTORS MENU-------")
        print("1.view patient")
        print("2. Add Medical record")
        print("3. add bill")
        print("4.Logout")
        
        choice = input("enter choice: ")
        
        if choice == "1":
            HospitalServices.view_patient()
            
        elif choice == "2":
            patient_id = int(input("Patient ID: "))
            diagnosis = input(" enter diagnosis: ")
            treatment = input("treatment :")
            prescription = input("enter prescription: ")
            date = input("visit date (YYYY-MM-DD): ")
            HospitalServices.add_medical_record(MedicalRecord(patient_id,diagnosis,treatment,prescription,date))
            
        elif choice == "3":
            patient_id = input("patient_id: ")
            amount = int(input("amount: "))
            payment_status = input("status: ")
            date = input("bill date (YYYY-MM-DD): ")
            HospitalServices.add_bills(Bills(patient_id,amount,payment_status,date))
        
        elif choice == "4":
            break 
        
        else:
            print("coose correct option -----")
            
            
def main():
    print("-------- HOSPITAL MANAGMENT SYSTEM---------")
    username = input("enter username: ")
    password = input("enter password: ")
    
    role = AuthService.login(username,password) 
    
    if not role:
        print("Invalid Credentials: ")
        return
    
    if role == "Admin":
        admin_menu()
    elif role == "Doctor":
        doctor_menu()
        
    elif role == "Rec":
        reception_menu()
        
if __name__ == "__main__":
    main()
          
            
            

    
    
    
            
            