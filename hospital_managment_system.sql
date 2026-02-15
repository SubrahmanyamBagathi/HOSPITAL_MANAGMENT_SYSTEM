create database hospital_db;

use hospital_db;

create table patients(
patient_id int  primary key auto_increment,
name varchar(50) not null,
age int not null,
gender varchar(20) not null,
phone bigint not null,
address text not null,
created_at timestamp default current_timestamp
);

create table doctor(
doctor_id int primary key auto_increment,
name varchar(100),
specialization varchar(100),
department varchar(100),
salary decimal(10,2),
phone varchar(15)
);



create table appointments(
appointment_id int primary key auto_increment,
doctor_id int,
patient_id int,
appointment_date date,
status varchar(100),
foreign key (doctor_id) REFERENCES doctor(doctor_id),
foreign key (patient_id) references patients(patient_id)
);

create table medical_records(
record_id int primary key auto_increment,
patient_id int,
diagnosis text,
treatment text,
prescription text,
visit_date date,
foreign key (patient_id) references patients(patient_id)
);


create table bills(
bill_id int primary key auto_increment,
patient_id int,
total_amount decimal(10,2),
payment_status varchar(50),
bill_date date,
foreign key (patient_id) references patients(patient_id)
);

show tables;


create table users (
user_id int primary key auto_increment,
username varchar(50) unique,
password varchar(30),
role varchar(20)
);


insert into users(username,password,role) values
('admin','admin123','Admin'),
('subbu', 'doc123', 'Doctor'),
('vinit', 'vinit123','Reception');


select * from users;

select * from patients;

select * from doctor;

insert into users(username,password,role) values
('rec','rec123','Rec');

select * from medical_records;

SHOW COLUMNS FROM appointments;

ALTER TABLE appointments
CHANGE appontment_date appointment_date DATE;

select * from bills;























