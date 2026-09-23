import streamlit as st
import csv
import os
from datetime import datetime

st.set_page_config(
    page_title="Personal Safety & Emergency Assistant",
    page_icon="🆘",
    layout="wide"
)

CONTACT_FILE = "emergency_contacts.csv"
INCIDENT_FILE = "incidents.csv"


# Create CSV files
def create_files():

    if not os.path.exists(CONTACT_FILE):
        with open(CONTACT_FILE, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Relationship", "Phone"])

    if not os.path.exists(INCIDENT_FILE):
        with open(INCIDENT_FILE, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(
                ["Date", "Incident Type", "Location", "Severity", "Description"]
            )


# Load contacts
def load_contacts():

    contacts = []

    with open(CONTACT_FILE, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            contacts.append(row)

    return contacts


# Load incidents
def load_incidents():

    incidents = []

    with open(INCIDENT_FILE, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            incidents.append(row)

    return incidents


# Save contact
def save_contact(name, relationship, phone):

    with open(CONTACT_FILE, "a", newline="", encoding="utf-8") as file:

        writer = csv.writer(file)

        writer.writerow([
            name,
            relationship,
            phone
        ])


# Save incident
def save_incident(incident_type, location, severity, description):

    with open(INCIDENT_FILE, "a", newline="", encoding="utf-8") as file:

        writer = csv.writer(file)

        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            incident_type,
            location,
            severity,
            description
        ])


# Create required files
create_files()

contacts = load_contacts()
incidents = load_incidents()


# Sidebar
st.sidebar.title("🆘 Safety Assistant")

st.sidebar.write(
    "Personal Safety & Emergency Support System"
)

menu = st.sidebar.radio(
    "Select Module",
    [
        "🏠 Dashboard",
        "👥 Emergency Contacts",
        "🚨 Emergency Alert",
        "📝 Report Incident",
        "📋 Incident History",
        "📞 Emergency Numbers",
        "🛡️ Safety Tips"
    ]
)


# Dashboard
if menu == "🏠 Dashboard":

    st.title("🆘 Personal Safety & Emergency Assistant")

    st.subheader("Your Safety Support Dashboard")

    st.write(
        "This application helps users manage emergency contacts, "
        "generate emergency messages, record incidents and "
        "access important safety information."
    )

    st.divider()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Emergency Contacts",
            len(contacts)
        )

    with col2:
        st.metric(
            "Reported Incidents",
            len(incidents)
        )

    with col3:
        st.metric(
            "Emergency Services",
            4
        )

    st.divider()

    st.subheader("🚨 Quick Emergency Action")

    st.info(
        "Use the Emergency Alert module to generate "
        "an emergency message quickly."
    )

    st.warning(
        "For real emergencies, contact the appropriate "
        "emergency service directly."
    )


# Emergency Contacts
elif menu == "👥 Emergency Contacts":

    st.title("👥 Emergency Contacts")

    st.subheader("Add Emergency Contact")

    with st.form("contact_form"):

        name = st.text_input("Contact Name")

        relationship = st.text_input("Relationship")

        phone = st.text_input(
            "Phone Number",
            placeholder="+919876543210"
        )

        submit = st.form_submit_button("➕ Add Contact")

        if submit:

            if not name or not relationship or not phone:

                st.error("Please fill all fields.")

            else:

                save_contact(
                    name.strip(),
                    relationship.strip(),
                    phone.strip()
                )

                st.success(
                    "Emergency contact added successfully!"
                )

                st.rerun()

    st.divider()

    st.subheader("📋 Saved Emergency Contacts")

    contacts = load_contacts()

    if contacts:

        for index, contact in enumerate(contacts, start=1):

            st.write(
                f"**{index}. {contact['Name']}**"
            )

            st.write(
                f"Relationship: {contact['Relationship']}"
            )

            st.write(
                f"Phone: {contact['Phone']}"
            )

            st.divider()

    else:

        st.info(
            "No emergency contacts added yet."
        )


# Emergency Alert
elif menu == "🚨 Emergency Alert":

    st.title("🚨 Emergency Alert Generator")

    st.warning(
        "This module generates an emergency message. "
        "It does not automatically send SMS."
    )

    contacts = load_contacts()

    if not contacts:

        st.error(
            "Please add an emergency contact first."
        )

    else:

        contact_names = [
            contact["Name"]
            for contact in contacts
        ]

        selected_name = st.selectbox(
            "Select Emergency Contact",
            contact_names
        )

        selected_contact = next(
            contact for contact in contacts
            if contact["Name"] == selected_name
        )

        st.info(
            f"Contact: {selected_contact['Name']} | "
            f"Phone: {selected_contact['Phone']}"
        )

        emergency_type = st.selectbox(
            "Emergency Type",
            [
                "Medical Emergency",
                "Accident",
                "Personal Threat",
                "Fire",
                "Harassment",
                "Missing Person",
                "Other"
            ]
        )

        location = st.text_input(
            "Current Location"
        )

        details = st.text_area(
            "Emergency Details"
        )

        if st.button("🚨 Generate Emergency Alert"):

            if not location or not details:

                st.error(
                    "Please enter location and emergency details."
                )

            else:

                message = (
                    "🚨 EMERGENCY ALERT 🚨\n\n"
                    f"Type: {emergency_type}\n"
                    f"Location: {location}\n"
                    f"Details: {details}\n\n"
                    "Please provide immediate assistance."
                )

                st.success(
                    "Emergency message generated successfully!"
                )

                st.subheader("📨 Emergency Message")

                st.text_area(
                    "Copy this message:",
                    message,
                    height=220
                )


# Report Incident
elif menu == "📝 Report Incident":

    st.title("📝 Report an Incident")

    incident_type = st.selectbox(
        "Incident Type",
        [
            "Harassment",
            "Accident",
            "Theft",
            "Personal Threat",
            "Cyber Incident",
            "Suspicious Activity",
            "Other"
        ]
    )

    location = st.text_input(
        "Incident Location"
    )

    severity = st.selectbox(
        "Severity",
        [
            "Low",
            "Medium",
            "High",
            "Critical"
        ]
    )

    description = st.text_area(
        "Incident Description"
    )

    if st.button("📝 Save Incident Report"):

        if not location or not description:

            st.error(
                "Please enter location and description."
            )

        else:

            save_incident(
                incident_type,
                location,
                severity,
                description
            )

            st.success(
                "Incident report saved successfully!"
            )

            st.rerun()


# Incident History
elif menu == "📋 Incident History":

    st.title("📋 Incident History")

    incidents = load_incidents()

    if not incidents:

        st.info(
            "No incidents have been reported."
        )

    else:

        for index, incident in enumerate(
            incidents,
            start=1
        ):

            st.subheader(
                f"Incident {index}"
            )

            st.write(
                f"**Date:** {incident['Date']}"
            )

            st.write(
                f"**Type:** {incident['Incident Type']}"
            )

            st.write(
                f"**Location:** {incident['Location']}"
            )

            st.write(
                f"**Severity:** {incident['Severity']}"
            )

            st.write(
                f"**Description:** {incident['Description']}"
            )

            st.divider()


# Emergency Numbers
elif menu == "📞 Emergency Numbers":

    st.title("📞 Emergency Numbers")

    emergency_numbers = [
        ("Emergency Services", "112"),
        ("Ambulance", "108"),
        ("Fire", "101"),
        ("Women Helpline", "181")
    ]

    for service, number in emergency_numbers:

        st.subheader(service)

        st.write(f"📞 {number}")

        st.divider()

    st.warning(
        "For an actual emergency, contact the "
        "appropriate emergency service directly."
    )


# Safety Tips
elif menu == "🛡️ Safety Tips":

    st.title("🛡️ Personal Safety Tips")

    st.subheader("🚶 Travel Safety")

    st.write("• Share your travel plans with a trusted person.")
    st.write("• Avoid isolated areas whenever possible.")
    st.write("• Keep your mobile phone charged.")
    st.write("• Keep emergency contacts easily accessible.")

    st.subheader("📱 Digital Safety")

    st.write("• Never share passwords or OTPs.")
    st.write("• Avoid suspicious links and unknown downloads.")
    st.write("• Use screen lock and device security.")

    st.subheader("🚨 During an Emergency")

    st.write("• Move to a safer location if possible.")
    st.write("• Contact the appropriate emergency service.")
    st.write("• Inform a trusted person about the situation.")

    st.subheader("🩺 Medical Emergency")

    st.write("• Seek professional medical assistance.")
    st.write("• Provide accurate information to emergency responders.")
    st.write("• Do not delay contacting emergency services.")