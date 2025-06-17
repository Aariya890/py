import datetime
import calendar
def show_month_calendar():
    try:
        year = int(input("Enter year(e.g. 2024): "))
        month = int(input("Enter month(1-12): "))
        print(calendar.month(year, month))
    except Exception:
        print("Invalid input.")

if __name__ == "__main__" :   
    show_month_calendar()