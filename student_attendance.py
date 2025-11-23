import datetime

FILE_NAME = "attendance.csv"

def mark_attendance():
    name = input("\nEnter student name: ").strip().title()
    today = datetime.date.today().strftime("%Y-%m-%d")

    try:
        with open(FILE_NAME, "r") as file:
            records = file.readlines()
            for line in records:
                if name in line and today in line:
                    print("⚠ Attendance already recorded for today.")
                    return
    except FileNotFoundError:
        pass

    with open(FILE_NAME, "a") as file:
        time_now = datetime.datetime.now().strftime("%H:%M:%S")
        file.write(f"{name},{today},{time_now}\n")

    print("✔ Attendance marked successfully!")

def view_attendance():
    print("\n📌 Attendance Records:")
    try:
        with open(FILE_NAME, "r") as file:
            data = file.readlines()
            if not data:
                print("No attendance data found.")
                return
            
            for record in data:
                print(record.strip())
    except FileNotFoundError:
        print("No attendance file found.")

def main():
    while True:
        print("\n===== STUDENT ATTENDANCE SYSTEM =====")
        print("1. Mark Attendance")
        print("2. View Attendance")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            mark_attendance()
        elif choice == "2":
            view_attendance()
        elif choice == "3":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Try again!")

main()