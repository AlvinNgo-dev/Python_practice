from datetime import datetime


def log_message(file_name):
    while True:
        message = input("Enter log message: ")
        if message == 'q':
            break
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(file_name, "a") as file:
            file.write(f"[{timestamp}] {message}\n")
        print("Message logged successfully.")


file_name = input("Enter log file name: ")
log_message(file_name)
