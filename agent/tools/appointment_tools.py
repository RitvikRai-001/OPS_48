from langchain_core.tools import tool
from agent.utils.api_client import api_get, api_post
from datetime import datetime, timezone


def make_appointment_tools(token: str):

    @tool
    def get_available_doctors(dummy_input: str = "") -> str:
        """
        Get the list of all available doctors the user can book an appointment with.
        Always call this FIRST before book_appointment so you know which doctors exist
        and can show their names and IDs to help the user pick one.
        No input needed — pass an empty string.
        """
        try:
            result = api_get("/api/v1/doctors", token)
            doctors = result.get("data", [])

            if not doctors:
                return "No doctors are currently available in the system."

            lines = []
            for d in doctors:
                lines.append(
                    f"- Dr. {d.get('username')} | "
                    f"Email: {d.get('email')} | "
                    f"Doctor ID: {d.get('_id')}"
                )
            return "Available doctors:\n" + "\n".join(lines)

        except Exception as e:
            return f"Error fetching doctors: {str(e)}"

    @tool
    def get_all_appointments(dummy_input: str = "") -> str:
        """
        Get all of the user's appointments — past and upcoming.
        Call this when the user asks to see all their appointments
        or their appointment history.
        No input needed — pass an empty string.
        """
        try:
            result = api_get("/api/v1/doctor-request/getappointments", token)
            appointments = result.get("data", [])

            if not appointments:
                return "You have no appointments on record."

            lines = []
            for a in appointments:
                doctor = a.get("doctorId", {})
                doc_name = doctor.get("username", "Unknown doctor") if isinstance(doctor, dict) else "Unknown doctor"
                lines.append(
                    f"- {a.get('appointmentDate', 'Unknown date')} | "
                    f"Dr. {doc_name} | "
                    f"Reason: {a.get('problem', 'Not specified')} | "
                    f"Status: {a.get('status', 'Unknown')}"
                )
            return "Your appointments:\n" + "\n".join(lines)

        except Exception as e:
            return f"Error fetching appointments: {str(e)}"

    @tool
    def get_upcoming_appointment(dummy_input: str = "") -> str:
        """
        Get the user's next upcoming appointment.
        Call this when the user asks when their next appointment is
        or whether they have any upcoming appointments.
        No input needed — pass an empty string.
        """
        try:
            result = api_get("/api/v1/doctor-request/getappointments", token)
            appointments = result.get("data", [])

            now = datetime.now(timezone.utc)
            upcoming = [
                a for a in appointments
                if a.get("appointmentDate") and
                datetime.fromisoformat(a["appointmentDate"].replace("Z", "+00:00")) > now
            ]

            if not upcoming:
                return "You have no upcoming appointments scheduled."

            apt = upcoming[0]
            doctor = apt.get("doctorId", {})
            doc_name = doctor.get("username", "your doctor") if isinstance(doctor, dict) else "your doctor"

            return (
                f"Your next appointment:\n"
                f"  📅 Date: {apt.get('appointmentDate')}\n"
                f"  👨‍⚕️ Doctor: Dr. {doc_name}\n"
                f"  📋 Reason: {apt.get('problem', 'Not specified')}\n"
                f"  Status: {apt.get('status')}"
            )

        except Exception as e:
            return f"Error fetching upcoming appointment: {str(e)}"


