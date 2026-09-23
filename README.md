# 🆘 Personal Safety & Emergency Assistant

## 📌 Project Description

Personal Safety & Emergency Assistant is a lightweight web-based application developed using **Python and Streamlit**.

The application helps users manage emergency contacts, generate emergency alert messages, report incidents, view incident history, access important emergency numbers, and read personal safety tips.

This project is designed as a simple academic application for demonstrating how Python and Streamlit can be used to develop a useful real-life safety-support system.

---

## 🎯 Objectives

* To provide a simple personal safety support platform.
* To maintain emergency contact information.
* To generate emergency alert messages quickly.
* To record and maintain incident details.
* To provide important emergency service numbers.
* To provide useful personal and digital safety tips.
* To demonstrate a lightweight Python and Streamlit application.

---

## ✨ Features

### 🏠 Dashboard

Displays:

* Number of emergency contacts
* Number of reported incidents
* Emergency service information
* Quick emergency guidance

### 👥 Emergency Contacts

Users can:

* Add emergency contacts
* Store name
* Store relationship
* Store phone number
* View saved contacts

### 🚨 Emergency Alert

Users can:

* Select an emergency contact
* Select emergency type
* Enter current location
* Enter emergency details
* Generate an emergency message

The generated message can be copied and manually sent through SMS or another messaging application.

### 📝 Incident Reporting

Users can record:

* Incident type
* Location
* Severity
* Description
* Date and time

### 📋 Incident History

Displays previously reported incidents.

### 📞 Emergency Numbers

Provides commonly used emergency numbers such as:

* Emergency Services – 112
* Ambulance – 108
* Fire – 101
* Women Helpline – 181

### 🛡️ Safety Tips

Provides basic guidance related to:

* Travel safety
* Digital safety
* Emergency situations
* Medical emergencies

---

## 🛠️ Technologies Used

* Python
* Streamlit
* CSV
* Python built-in modules

### Python Built-in Modules

* `csv`
* `os`
* `datetime`

---

## 📦 Required Package

Only one external Python package is required:

```text
streamlit
```

The project does not require:

* Pandas
* Twilio
* python-dotenv
* Any SMS API

---

## 📁 Project Structure

```text
Personal-Safety-Emergency-Assistant
│
├── app.py
├── emergency_contacts.csv
├── incidents.csv
├── requirements.txt
├── .gitignore
└── venv
```

---

## ▶️ How to Run the Project

### Step 1: Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### Step 2: Open the project folder

```bash
cd Personal-Safety-Emergency-Assistant
```

### Step 3: Create virtual environment

```bash
python -m venv venv
```

### Step 4: Activate virtual environment

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### Step 5: Install Streamlit

```bash
python -m pip install streamlit
```

### Step 6: Run the application

```bash
python -m streamlit run app.py
```

The application will open in the web browser.

---

## 💾 Data Storage

The application uses CSV files for simple local data storage.

### emergency_contacts.csv

Stores:

* Name
* Relationship
* Phone Number

### incidents.csv

Stores:

* Date
* Incident Type
* Location
* Severity
* Description

No database server is required.

---

## ⚠️ Important Note

This project is an academic safety-support application.

The Emergency Alert module **generates an emergency message but does not automatically send SMS messages**.

For real emergencies, users should contact the appropriate emergency service directly.

---

## 🚀 Future Enhancements

Future versions can include:

* Automatic SMS alerts
* GPS-based location sharing
* Mobile application version
* User login and authentication
* Database integration
* Emergency alert notifications
* Interactive safety map
* Cloud-based data storage
* AI-based emergency assistance

---

## 👩‍💻 Project Type

**Application-Oriented Python & Streamlit Project**

## 📚 Purpose

Developed as an academic project to demonstrate the practical use of Python programming and Streamlit for solving real-life problems.
