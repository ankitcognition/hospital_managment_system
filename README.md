# Hospital Management System (Python)

A console-based Hospital Management System built using Python.

This project is part of my Python learning journey and is being developed incrementally to simulate real-world software development while improving programming and problem-solving skills.

## Current Status

**Patient Management Completed | Doctor Management Completed | Appointment Management Completed | Billing System In Progress**

## Completed Features

* Patient registration
* Patient ID input
* Patient name input
* Patient age input
* Patient gender input
* Patient phone number input
* Patient blood group input
* Patient disease input
* Patient admission date input
* Input validation using `try` / `except`
* CSV file handling
* Patient data storage using CSV
* Append-based patient record storage
* View all registered patients
* Handle empty patient records
* Formatted patient information display
* Search patient by Patient ID
* Display searched patient information
* Handle patient not found cases
* Update patient information
* Search and edit existing patient records
* Rewrite updated records back to CSV
* Delete patient records by Patient ID
* Delete confirmation before removing a patient
* Rewrite remaining patient records back to CSV after deletion
* Doctor CSV file setup
* Doctor ID input
* Doctor name input
* Doctor specialization input
* Doctor ID input validation
* Append-based doctor record storage
* Search doctor by Doctor ID
* Display searched doctor information
* Handle doctor not found cases
* View all registered doctors
* Handle empty doctor records
* Display formatted doctor information
* Search doctor by ID for update
* Handle doctor not found during update
* Display doctor menu (ID / Name / Specialization)
* Update menu choice validation
* Update doctor ID
* Update doctor name
* Update doctor specialization
* Display updated doctor information
* Rewrite doctor CSV header after update
* Rewrite updated doctor records back to CSV
* Search doctor by ID for deletion
* Display doctor details before deletion
* Handle doctor not found during deletion
* Delete confirmation before removing a doctor (Y/N)
* Handle invalid confirmation input
* Cancel deletion on user choice
* Remove doctor record from list
* Rewrite doctor CSV header after deletion
* Rewrite remaining doctor records back to CSV after deletion
* Appointment CSV file setup
* Appointment ID input
* Appointment ID validation
* Duplicate appointment ID prevention
* Patient ID input and validation for appointment
* Verify patient exists before booking
* Doctor ID input and validation for appointment
* Verify doctor exists before booking
* Appointment date input
* Appointment time input
* Default appointment status ("Scheduled")
* Append-based appointment record storage
* View all registered appointments
* Handle empty appointment records
* Formatted appointment information display
* Search appointment by Appointment ID
* Display searched appointment information
* Handle appointment not found cases
* Search appointment by ID for update
* Handle appointment not found during update
* Display appointment update menu (Date / Time / Status)
* Update menu choice validation
* Update appointment date
* Update appointment time
* Update appointment status
* Display updated appointment information
* Rewrite appointment CSV header after update
* Rewrite updated appointment records back to CSV
* Search appointment by ID for deletion
* Display appointment details before deletion
* Handle appointment not found during deletion
* Delete confirmation before removing an appointment (Y/N)
* Handle invalid confirmation input
* Cancel deletion on user choice
* Remove appointment record from list
* Rewrite appointment CSV header after deletion
* Rewrite remaining appointment records back to CSV after deletion
* Bill CSV file setup

## Possible Improvements

* Improve input validation
* Add duplicate patient ID prevention
* Add duplicate doctor ID prevention
* Add hospital statistics
* Improve date validation
* Fix update doctor crash when doctor ID is not found
* Fix delete doctor crash when doctor ID is not found
* Fix appointment CSV setup overwriting existing data on every run
* Fix billing CSV setup overwriting existing data on every run

## Technologies Used

* Python 3
* CSV

## How to Run

1. Clone the repository.

```bash
git clone <repository-url>
```

2. Navigate to the project folder.

```bash
cd Hospital-Management-System
```

3. Run the program.

```bash
python main.py
```

## Learning Objectives

This project is being built to strengthen understanding of:

* Functions
* User Input
* Conditional Statements
* Exception Handling
* File Handling
* CSV Module
* Lists
* Variables and Data Types
* CRUD Operations
* Input Validation
* Problem Solving
* Program Design

## Development Progress

* [x] Project setup
* [x] Patient CSV file setup
* [x] Patient registration
* [x] Patient input handling
* [x] Input validation
* [x] CSV data storage
* [x] View All Patients
* [x] Handle empty patient records
* [x] Formatted patient information
* [x] Search Patient
* [x] Handle patient not found
* [x] Update Patient
* [x] Delete Patient
* [x] Delete confirmation
* [x] Rewrite CSV after patient deletion
* [x] Doctor CSV file setup
* [x] Doctor registration
* [x] Doctor input validation
* [x] Doctor CSV data storage
* [x] Search Doctor
* [x] Handle doctor not found
* [x] View All Doctors
* [x] Handle empty doctor records
* [x] Formatted doctor information
* [x] Search doctor by ID for update
* [x] Handle doctor not found during update
* [x] Doctor update menu
* [x] Update doctor ID
* [x] Update doctor name
* [x] Update doctor specialization
* [x] Rewrite doctor CSV after update
* [x] Search doctor by ID for deletion
* [x] Delete confirmation
* [x] Rewrite CSV after doctor deletion
* [x] Appointment CSV file setup
* [x] Appointment registration
* [x] Appointment ID validation
* [x] Duplicate appointment ID check
* [x] Patient existence check
* [x] Doctor existence check
* [x] View All Appointments
* [x] Handle empty appointment records
* [x] Formatted appointment information
* [x] Search Appointment
* [x] Handle appointment not found
* [x] Search appointment by ID for update
* [x] Handle appointment not found during update
* [x] Appointment update menu
* [x] Update appointment date
* [x] Update appointment time
* [x] Update appointment status
* [x] Rewrite appointment CSV after update
* [x] Search appointment by ID for deletion
* [x] Delete confirmation
* [x] Rewrite CSV after appointment deletion
* [x] Bill CSV file setup
* [ ] Generate Bill
* [ ] View All Bills
* [ ] Search Bill
* [ ] Delete Bill
* [ ] Hospital Statistics
* [ ] Final Testing
* [ ] Documentation Improvements

## License

This project is intended for learning and educational purposes.