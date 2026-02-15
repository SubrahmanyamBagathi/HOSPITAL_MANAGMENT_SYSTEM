
class Person:
    def __init__(self,name,age,phone):
        self.name = name
        self.age = age
        self.phone = phone
        
class Patient(Person):
    def __init__(self,name,age,gender,phone,address):
        super().__init__(name,age,phone)
        self.gender = gender
        self.address = address
        
        
class Doctor():
    def __init__(self,name,phone,specialization,department,salary):
        self.name = name
        self.phone = phone
        self.specialization = specialization
        self.department = department
        self.salary = salary
        

class Appontment:
    def __init__(self,patient_id,doctor_id,appointment_date,status):
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.appointment_date = appointment_date
        self.status = status
        

class MedicalRecord:
    def __init__(self,patient_id,diagnosis,treatment,prescription,visit_date):
        self.patient_id = patient_id
        self.diagnosis = diagnosis
        self.treatment = treatment
        self.prescription = prescription
        self.visit_date = visit_date
        
class Bills:
    def __init__(self,patient_id,total_amount,payment_status,bill_date):
        self.patient_id = patient_id
        self.total_amount = total_amount
        self.payment_status = payment_status
        self.bill_date = bill_date
        
    def __str__():
        return f"bill for patient {self.patient_id} - {self.total_amount} - {self.payment_status}" # type: ignore