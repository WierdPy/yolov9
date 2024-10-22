import requests

apisend= False

def notify_person_event(event_type):
    """
    Sends a notification to the API about a person entering or exiting.
    :param event_type: 'enter' for entering the frame, 'exit' for exiting the frame.
    """
    url = "https://ntfy.sh/Sagasu"
    data = event_type  # send 'enter' or 'exit' as data
    if apisend:
        try:
            response = requests.post(url, data=data)
            response.raise_for_status()
            #print(f"Notification sent: {event_type}")
        except requests.exceptions.RequestException as e:
            #print(f"Failed to send notification: {e}")
            pass
