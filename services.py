

from database import DatabaseManager
from models import Patient,Doctor,Bills,MedicalRecord,Appontment



db = DatabaseManager()

class AuthService:
    
    @staticmethod
    def login(username,password):
        query = "select role from users where username=%s and password=%s"
        db.execute(query,(username,password))
        result = db.fetch_one()
        return result[0] if result else None
    

class HospitalServices:
    
    
     # ----------------Patient-------------
     
    @staticmethod
    def add_patient(patient:Patient):
        query = "insert into patients (name,age,phone,gender,address) values (%s,%s,%s,%s,%s)"
        db.execute(query,(patient.name,patient.age,patient.phone,patient.gender,patient.address))
        db.commit()
        print("patient added succesfully")
         
    @staticmethod  
    def view_patient():
        query = "select * from patients"
        db.execute(query)
        for row in db.fetch_all():
            print(row)
             
             
    # ---------------Doctor----------------------
    
    @staticmethod
    def add_doctor(Doctor:Doctor):
        query = "insert into doctor (name,phone,specialization,department,salary) values(%s,%s,%s,%s,%s)"    
        db.execute(query,(Doctor.name,Doctor.phone,Doctor.specialization,Doctor.department,Doctor.salary))
        db.commit()
        print("Doctor added succesfully")
        
    @staticmethod
    def view_doctor():
        db.execute("select * from doctor") 
        for row in db.fetch_all():
            print(row)
            
            
    # -------------------Appontment------------------
    
    @staticmethod
    def book_appointment(appointment:Appontment):
        query = "insert into appointments (doctor_id,patient_id,appointment_date,status) values(%s,%s,%s,%s)"
        db.execute(query,(appointment.doctor_id,appointment.patient_id,appointment.appointment_date,appointment.status))
        db.commit()  
        print("appointment booked succesfully")
        
    @staticmethod
    def view_appointment():
        query = """
         select a.appointment_id,p.name,d.name,a.appointment_date,a.status
         from appointments a
         join patients p on a.patient_id = p.patient_id
         join doctor d on a.doctor_id = d.doctor_id
        """
        
        db.execute(query)
        for row in db.fetch_all():
            print(row)
            
            
    # --------------------Medical Record------------------------
    
    @staticmethod
    def add_medical_record(MedicalRecord:MedicalRecord):
        query = """
        insert into medical_records (patient_id,diagnosis,treatment,prescription,visit_date)
        values (%s,%s,%s,%s,%s)
        """
        
        db.execute(query,(MedicalRecord.patient_id,MedicalRecord.diagnosis,MedicalRecord.treatment,MedicalRecord.prescription,MedicalRecord.visit_date))
        db.commit()
        print("medical record added succesfully")
        
        
    @staticmethod
    
    def view_medical_record():
        
        query = """
        select m.record_id,p.name,m.diagnosis,m.visit_date
        from medical_record m
        join patients on m.patient_id = p.patient_id
        """
        
        db.execute(query)
        for row in db.fetch_all():
            print(row)
            
            
            
    # ------------------------Bills ------------------------------
    
    @staticmethod
    def add_bills(Bills:Bills):
        query = """
        insert into bills (patient_id,total_amount,payment_status,bill_date)
        values (%s,%s,%s,%s)
        """
        
        db.execute(query,(Bills.patient_id,Bills.total_amount,Bills.payment_status,Bills.bill_date))
        db.commit()
        print("bill added succesfully")
        
        
    @staticmethod
    
    def view_bill():
        query = """
        select b.bill_id,p.name,b.total_amount,b.payment_status,b.bill_date
        from bills b
        join patients p on b.patient_id = p.patient_id
        """
        
        db.execute(query)
        for row in db.fetch_all():
            print(row)