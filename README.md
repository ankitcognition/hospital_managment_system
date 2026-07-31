# Hospital Management System (Python)

A console-based Hospital Management System built using Python and CSV file storage. Manage patients, doctors, appointments, and billing — all from the terminal.

This project was built incrementally as a learning exercise to practice real-world program structure, file handling, and CRUD operations in Python.

## Overview

The system is organized into four core modules, each supporting full CRUD (Create, Read, Update, Delete) operations backed by its own CSV file:

- **Patients** — registration, records, updates, deletion
- **Doctors** — registration, records, updates, deletion
- **Appointments** — booking, tracking, updates, cancellation (with patient/doctor validation)
- **Billing** — bill generation, records, deletion (with automatic total calculation)

A **Hospital Statistics** view summarizes total counts across all four modules.

## Features

### Patient Management
- Register patients (ID, name, age, gender, phone, blood group, disease, admission date)
- View all patients / handle empty records
- Search patient by ID
- Update patient information (any field)
- Delete patient with confirmation

### Doctor Management
- Register doctors (ID, name, specialization)
- View all doctors / handle empty records
- Search doctor by ID
- Update doctor information (any field)
- Delete doctor with confirmation

### Appointment Management
- Book appointments, linked to existing patient and doctor records
- Duplicate appointment ID prevention
- Validates that referenced patient and doctor exist before booking
- View all appointments / handle empty records
- Search appointment by ID
- Update appointment date, time, or status
- Delete appointment with confirmation

### Billing System
- Generate bills, linked to existing patient and doctor records
- Duplicate bill ID prevention
- Validates that referenced patient and doctor exist before billing
- Automatic total amount calculation (consultation + medicine + other charges)
- View all bills / handle empty records
- Search bill by ID
- Delete bill with confirmation

### Hospital Statistics
- Total registered patients, doctors, appointments, and bills at a glance

## Technologies Used

- Python 3
- CSV module (file-based data storage, no external database)

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

## Testing

All 15 core functions were tested against 46 scenarios, covering valid input, invalid input (non-numeric IDs), not-found records, duplicate IDs, and delete confirm/cancel paths. All scenarios completed without crashing, and output data was verified against expected CSV state.

## Known Issues / Possible Improvements

- **CSV setup blocks overwrite existing data on every run.** The setup code for each CSV file currently runs unconditionally in `"w"` mode, so restarting the program erases all records. Should be wrapped in an `if not os.path.exists(...)` check.
- No duplicate ID prevention on patient or doctor registration (appointments and bills already have this).
- Minimal ID validation — no check for negative numbers or zero.
- Free-text date/time fields with no format validation.
- No appointment or bill editing beyond the fields currently supported (e.g., no "Update Bill").

## Planned Additions

- Fix CSV overwrite-on-startup issue
- Add duplicate ID prevention for patients and doctors
- Improve date/time input validation
- Final documentation pass

## Learning Objectives

This project was built to strengthen understanding of:

- Functions
- User input handling
- Conditional statements
- Exception handling
- File handling
- CSV module
- Lists
- Variables and data types
- CRUD operations
- Input validation
- Problem solving
- Program design

## License

This project is intended for learning and educational purposes.