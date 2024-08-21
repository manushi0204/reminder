import time
from plyer import notification

def send_water_reminder():
    notification.notify(
        title='Water Reminder',
        message='Time to drink some water!',
        app_name='Water Reminder',
        timeout=10  # Notification duration in seconds
    )

def main():
    # Define the interval in seconds (e.g., 3600 seconds = 1 hour)
    reminder_interval = 3600
    
    print("Water Reminder is running. Press Ctrl+C to exit.")
    try:
        while True:
            send_water_reminder()
            time.sleep(reminder_interval)
    except KeyboardInterrupt:
        print("Water Reminder stopped.")

if __name__ == '__main__':
    main()
 