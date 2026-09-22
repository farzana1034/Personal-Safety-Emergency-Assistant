import streamlit as st
import pandas as pd
import os
from datetime import datetime
from dotenv import load_dotenv
from twilio.rest import Client


# =========================================================
# LOAD ENVIRONMENT VARIABLES
# =========================================================

load_dotenv()

TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_PHONE_NUMBER = os.getenv("TWILIO_PHONE_NUMBER")


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Personal Safety & Emergency Assistant",
    page_icon="🆘",
    layout="wide"
)


# =========================================================
# FILE NAMES
# =========================================================

CONTACT_FILE = "emergency_contacts.csv"
INCIDENT_FILE = "incidents.csv"


# =========================================================
# CREATE CSV FILES IF THEY DON'T EXIST
# =========================================================

if not os.path.exists(CONTACT_FILE):

    contacts_df = pd.DataFrame(
        columns=[
            "Name",
            "Relationship",
            "Phone"
        ]
    )

    contacts_df.to_csv(
        CONTACT_FILE,
        index=False
    )


if not os.path.exists(INCIDENT_FILE):

    incidents_df = pd.DataFrame(
        columns=[
            "Date",
            "Incident Type",
            "Location",
            "Severity",
            "Description"
        ]
    )

    incidents_df.to_csv(
        INCIDENT_FILE,
        index=False
    )


# =========================================================
# LOAD DATA
# =========================================================

contacts_df = pd.read_csv(CONTACT_FILE)

incidents_df = pd.read_csv(INCIDENT_FILE)


# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.title("🆘 Safety Assistant")

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


# =========================================================
# DASHBOARD
# =========================================================

if menu == "🏠 Dashboard":

    st.title(
        "🆘 Personal Safety & Emergency Assistant"
    )

    st.subheader(
        "Your Safety Support Dashboard"
    )

    st.write(
        "This application provides basic safety assistance "
        "through emergency contacts, emergency alerts, "
        "incident reporting, emergency numbers and safety tips."
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "Emergency Contacts",
            len(contacts_df)
        )

    with col2:

        st.metric(
            "Reported Incidents",
            len(incidents_df)
        )

    with col3:

        st.metric(
            "Emergency Services",
            4
        )

    st.divider()

    st.subheader(
        "🚨 Quick Emergency Actions"
    )

    st.info(
        "Use the Emergency Alert module to generate and "
        "send an emergency SMS to a saved emergency contact."
    )

    st.divider()

    st.subheader("⚠️ Important")

    st.warning(
        "Emergency SMS functionality requires a properly "
        "configured Twilio account and verified recipient."
    )


# =========================================================
# EMERGENCY CONTACTS
# =========================================================

elif menu == "👥 Emergency Contacts":

    st.title(
        "👥 Emergency Contacts"
    )

    st.subheader(
        "Add Emergency Contact"
    )

    with st.form("contact_form"):

        name = st.text_input(
            "Contact Name"
        )

        relationship = st.text_input(
            "Relationship"
        )

        phone = st.text_input(
            "Phone Number",
            placeholder="+919876543210"
        )

        submit = st.form_submit_button(
            "➕ Add Contact"
        )

        if submit:

            if name and relationship and phone:

                new_contact = pd.DataFrame(
                    [{
                        "Name": name,
                        "Relationship": relationship,
                        "Phone": phone
                    }]
                )

                contacts_df = pd.concat(
                    [
                        contacts_df,
                        new_contact
                    ],
                    ignore_index=True
                )

                contacts_df.to_csv(
                    CONTACT_FILE,
                    index=False
                )

                st.success(
                    "Emergency contact added successfully!"
                )

                st.rerun()

            else:

                st.error(
                    "Please fill all fields."
                )

    st.divider()

    st.subheader(
        "📋 Saved Emergency Contacts"
    )

    if len(contacts_df) > 0:

        st.dataframe(
            contacts_df,
            use_container_width=True
        )

    else:

        st.info(
            "No emergency contacts added yet."
        )


# =========================================================
# EMERGENCY ALERT + SMS
# =========================================================

elif menu == "🚨 Emergency Alert":

    st.title(
        "🚨 Emergency Alert"
    )

    st.warning(
        "Use this module to generate an emergency message "
        "and send it to a saved emergency contact."
    )

    if len(contacts_df) == 0:

        st.error(
            "Please add at least one emergency contact first."
        )

    else:

        contact_names = contacts_df["Name"].tolist()

        selected_name = st.selectbox(
            "Select Emergency Contact",
            contact_names
        )

        selected_contact = contacts_df[
            contacts_df["Name"] == selected_name
        ].iloc[0]

        recipient_number = selected_contact["Phone"]

        st.info(
            f"SMS will be sent to: {recipient_number}"
        )

        emergency_type = st.selectbox(
            "Select Emergency Type",
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
            "Enter Current Location"
        )

        details = st.text_area(
            "Describe the Emergency"
        )

        if st.button(
            "🚨 Send Emergency SMS"
        ):

            if not location or not details:

                st.error(
                    "Please enter location and emergency details."
                )

            elif not recipient_number.startswith("+"):

                st.error(
                    "Please store the phone number in E.164 format, "
                    "for example +919876543210."
                )

            elif not TWILIO_ACCOUNT_SID or not TWILIO_AUTH_TOKEN or not TWILIO_PHONE_NUMBER:

                st.error(
                    "Twilio credentials are not configured. "
                    "Please check your .env file."
                )

            else:

                emergency_message = (
                    "EMERGENCY ALERT\n\n"
                    f"Type: {emergency_type}\n"
                    f"Location: {location}\n"
                    f"Details: {details}\n\n"
                    "Please provide immediate assistance."
                )

                try:

                    client = Client(
                        TWILIO_ACCOUNT_SID,
                        TWILIO_AUTH_TOKEN
                    )

                    message = client.messages.create(
                        body=emergency_message,
                        from_=TWILIO_PHONE_NUMBER,
                        to=recipient_number
                    )

                    st.success(
                        "✅ Emergency SMS sent successfully!"
                    )

                    st.write(
                        f"Message SID: {message.sid}"
                    )

                    st.subheader(
                        "📨 Message Sent"
                    )

                    st.info(
                        emergency_message
                    )

                except Exception as e:

                    st.error(
                        "❌ SMS could not be sent."
                    )

                    st.write(
                        f"Error: {e}"
                    )


# =========================================================
# REPORT INCIDENT
# =========================================================

elif menu == "📝 Report Incident":

    st.title(
        "📝 Report an Incident"
    )

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

    if st.button(
        "📝 Save Incident Report"
    ):

        if location and description:

            new_incident = pd.DataFrame(
                [{
                    "Date": datetime.now().strftime(
                        "%Y-%m-%d %H:%M:%S"
                    ),
                    "Incident Type": incident_type,
                    "Location": location,
                    "Severity": severity,
                    "Description": description
                }]
            )

            incidents_df = pd.concat(
                [
                    incidents_df,
                    new_incident
                ],
                ignore_index=True
            )

            incidents_df.to_csv(
                INCIDENT_FILE,
                index=False
            )

            st.success(
                "Incident report saved successfully!"
            )

            st.rerun()

        else:

            st.error(
                "Please enter location and description."
            )


# =========================================================
# INCIDENT HISTORY
# =========================================================

elif menu == "📋 Incident History":

    st.title(
        "📋 Incident History"
    )

    if len(incidents_df) > 0:

        st.dataframe(
            incidents_df,
            use_container_width=True
        )

        st.subheader(
            "📊 Incident Summary"
        )

        type_counts = incidents_df[
            "Incident Type"
        ].value_counts()

        st.bar_chart(
            type_counts
        )

    else:

        st.info(
            "No incidents have been reported."
        )


# =========================================================
# EMERGENCY NUMBERS
# =========================================================

elif menu == "📞 Emergency Numbers":

    st.title(
        "📞 Emergency Numbers"
    )

    emergency_numbers = pd.DataFrame(
        {
            "Service": [
                "Emergency Services",
                "Ambulance",
                "Fire",
                "Women Helpline"
            ],
            "Number": [
                "112",
                "108",
                "101",
                "181"
            ]
        }
    )

    st.table(
        emergency_numbers
    )

    st.warning(
        "For an actual emergency, contact the appropriate "
        "emergency service directly."
    )


# =========================================================
# SAFETY TIPS
# =========================================================

elif menu == "🛡️ Safety Tips":

    st.title(
        "🛡️ Personal Safety Tips"
    )

    st.subheader(
        "🚶 Travel Safety"
    )

    st.write(
        "• Share your travel plans with a trusted person."
    )

    st.write(
        "• Avoid isolated areas when possible."
    )

    st.write(
        "• Keep your phone charged."
    )

    st.subheader(
        "📱 Digital Safety"
    )

    st.write(
        "• Do not share passwords or OTPs."
    )

    st.write(
        "• Avoid clicking suspicious links."
    )

    st.write(
        "• Use screen lock and device security."
    )

    st.subheader(
        "🚨 During an Emergency"
    )

    st.write(
        "• Move to a safer location if possible."
    )

    st.write(
        "• Contact appropriate emergency services."
    )

    st.write(
        "• Inform a trusted person about the situation."
    )

    st.subheader(
        "🩺 Medical Emergency"
    )

    st.write(
        "• Seek professional medical assistance."
    )

    st.write(
        "• Provide accurate information to emergency responders."
    )