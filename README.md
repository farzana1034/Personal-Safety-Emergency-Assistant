# 🆘 Personal Safety & Emergency Assistant

## 📌 Project Description

Personal Safety & Emergency Assistant is a Python and Streamlit-based application designed to provide basic safety assistance during emergency situations.

The application allows users to manage emergency contacts, generate simulated emergency alerts, report and track incidents, view important emergency numbers, and access personal safety guidelines.

This project demonstrates how Python and Streamlit can be used to develop a practical, user-friendly daily-life application.

## 🎯 Objectives

* Provide a simple personal safety assistance platform.
* Maintain important emergency contact information.
* Generate emergency alert messages quickly.
* Record and manage incident details.
* Provide easy access to emergency numbers.
* Provide basic personal safety guidelines.
* Demonstrate Python, Streamlit, Pandas, and CSV data storage.

## 🚀 Features

### 🏠 Dashboard

* Emergency contact count
* Reported incident count
* Quick access to safety modules

### 👥 Emergency Contacts

* Add emergency contacts
* Store name, relationship, and phone number
* View saved contacts

### 🚨 Emergency Alert

* Select emergency type
* Enter location
* Enter emergency details
* Generate a simulated emergency message

### 📝 Incident Reporting

* Record different types of incidents
* Store date and time
* Record location and description
* Select incident severity

### 📋 Incident History

* View reported incidents
* Display incident information in a table
* View incident summary chart

### 📞 Emergency Numbers

The application provides quick access to commonly used emergency numbers.

### 🛡️ Safety Tips

Provides basic guidance related to travel safety, digital safety, emergencies, and medical emergencies.

## 🛠️ Technologies Used

* Python
* Streamlit
* Pandas
* CSV
* VS Code
* Git
* GitHub

## 📂 Project Structure

```text
Personal-Safety-Emergency-Assistant/
│
├── app.py
├── emergency_contacts.csv
├── incidents.csv
├── requirements.txt
├── README.md
└── .gitignore
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Open the project folder

```bash
cd Personal-Safety-Emergency-Assistant
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

For Windows PowerShell:

```powershell
venv\Scripts\activate
```

### 5. Install required packages

```powershell
python -m pip install -r requirements.txt
```

## ▶️ Run the Application

```powershell
streamlit run app.py
```

The application will open in a web browser.

## 💾 Data Storage

The application uses CSV files for simple local data storage.

### emergency_contacts.csv

Stores:

* Contact Name
* Relationship
* Phone Number

### incidents.csv

Stores:

* Date
* Incident Type
* Location
* Severity
* Description

## ⚠️ Important Note

This project is an educational and simulated safety-assistance application.

The Emergency Alert module only generates an emergency message. It does not automatically send SMS messages, make phone calls, track GPS location, or directly contact emergency services.

For an actual emergency, users should contact the appropriate emergency service directly.

## 🔮 Future Enhancements

* GPS-based location detection
* SMS alert integration
* Email notifications
* User authentication
* Cloud database
* Nearby hospital and police station search
* Voice-based SOS activation
* AI-based emergency classification
* One-click SOS functionality
* Mobile application support

## 🎓 Academic Application

This project demonstrates:

* Python programming
* Streamlit web application development
* Data handling using Pandas
* CSV-based storage
* User interface design
* Problem-solving
* Git and GitHub version control

## 👩‍💻 Project Type

**Application-Oriented Daily-Life Safety Project**

### Developed Using

**Python + Streamlit + Pandas**

### 📱 Emergency SMS
- Select a saved emergency contact.
- Generate an emergency message.
- Send the emergency alert through Twilio SMS.
- Display the message SID after successful submission.
## ⚠️ Important Note

This project is an educational safety-assistance application.

The Emergency Alert module can send SMS messages through the Twilio
Messaging API when valid Twilio credentials and an eligible recipient
are configured.

Twilio trial accounts have restrictions such as verified recipients
and other trial limitations.

For actual emergencies, users should contact the appropriate emergency
service directly.