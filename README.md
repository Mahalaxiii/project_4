Project 7: Hospital Patient Records System - README
Overview
The Hospital Patient Records System is a robust command-line application developed in Python as part of the Machine Learning September 2026 training curriculum minor projects. It streamlines medical record management, allowing healthcare staff to register patients, search medical histories, update diagnostic details, discharge or remove patient entries, and persist records securely across sessions.

Main Features Implemented
Register Patients: Add new patient profiles with unique IDs, names, age, contact information, and initial diagnosis details.

Search Patients: Quickly query and retrieve patient records by ID, name, or medical condition.

Update Patient Records: Modify existing patient information, including treatment progress, prescriptions, and room assignments.

Delete Patient Records: Archive or remove patient files upon discharge or administrative request.

Data Persistence: Automatically save and load patient databases using persistent storage files to maintain data integrity across program runs.

Classes Used
Following object-oriented programming (OOP) principles, the project implements the following core classes:

Person (Base Class): Encapsulates shared demographic attributes (name, age, contact) applicable to individuals in the hospital system.

Patient (Derived Class): Inherits from Person and adds patient-specific attributes (patient_id, diagnosis, medical_history, admission_status) and specialized methods.

HospitalSystem (Management Class): Orchestrates the collection of patient records, handles user menu navigation, enforces validation rules, and manages file I/O operations for data persistence.

How the Project Works
Initialization: Upon launching, the application reads stored data files to load existing patient records into memory.

Menu-Driven Interface: The program provides an interactive console menu allowing staff to choose tasks such as registering patients, searching records, updating details, or managing discharges.

Validation & Exception Handling: User inputs are strictly validated to prevent crashes caused by invalid ID formats, negative ages, or missing fields. Custom exception handlers manage file errors smoothly.

Persistence: Every new registration, update, or deletion updates internal collections and saves the modified state to persistent storage.

How to Run the Project
Prerequisites
Python 3.8 or higher installed on your system.

Standard Python libraries (no external dependencies required).

Execution Steps
Clone the repository or download all project files into a local directory.

Open your terminal or command prompt and navigate to the project root directory:

Bash
cd hospital-patient-records-system
Run the main application script:

Bash
python main.py
Follow the on-screen prompts in the interactive console to operate the system
