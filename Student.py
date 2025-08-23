import pandas as pd


file_path = "C:/Users/shrab/Downloads/student_scores.xlsx"   # <-- Change path if the file is in another location
df = pd.read_excel(file_path)


print(df.head())


subjects = ["Mathematics", "English", "Physics", "Chemistry", "Biology"]

df["Total"] = df[subjects].sum(axis=1)
df["Average"] = df[subjects].mean(axis=1)
df["Percentage"] = (df["Total"] / (len(subjects) * 100)) * 100  
r
def student_report(roll_number):
    if roll_number not in df["Roll Number"].values:
        return f"Roll Number {roll_number} not found."
    
    student = df[df["Roll Number"] == roll_number].iloc[0]
    
    report = f"""
    📘 Report for Roll Number: {student['Roll Number']}
    ------------------------------------------
    Total Marks   : {student['Total']}
    Average Score : {student['Average']:.2f}
    Percentage    : {student['Percentage']:.2f}%
    """
    
    failed_courses = [sub for sub in subjects if student[sub] < 50]
    if failed_courses:
        report += "\n❌ Failed in: " + ", ".join(failed_courses)
    else:
        report += "\n✅ Passed all courses"
    
    return report

print(student_report("R005"))

def highest_marks():
    sub = input("Enter the subject name: ")
    if sub in df.columns:
      highest_mark = df[sub].max()
      roll_numbers = df[df[sub] == highest_mark]["Roll Number"].tolist()
      for roll in roll_numbers:
        print(f"Roll number {roll} got the highest marks in {sub} and the highest mark is ({highest_mark})")
    else:
        print(f"Subject {sub} is not found.")

highest_marks()    

