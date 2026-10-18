"""
Student Performance Analytics System
Beginner-friendly project using Python, NumPy, and Pandas.
Run with: python main.py
"""

import numpy as np
import pandas as pd

DATA_FILE = "students.csv"
SUBJECTS = ["Math", "Physics", "Chemistry", "English", "Computer_Science"]
PASS_MARK = 35


def assign_grade(average):
    """Return a grade based on the student's average marks."""
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"


def check_pass_fail(row):
    """A student passes only if they score at least 35 in every subject."""
    for subject in SUBJECTS:
        if row[subject] < PASS_MARK:
            return "Fail"
    return "Pass"


def load_student_data(filename):
    """Load the CSV dataset into a Pandas DataFrame."""
    try:
        data = pd.read_csv(filename)
    except FileNotFoundError:
        print(f"Error: Could not find '{filename}'.")
        print("Keep main.py and students.csv in the same folder.")
        return None

    required_columns = ["Student_ID", "Name", "Department"] + SUBJECTS + ["Attendance_Percent"]
    missing_columns = [column for column in required_columns if column not in data.columns]

    if missing_columns:
        print("Error: These required columns are missing:", missing_columns)
        return None

    return data


def analyze_students(data):
    """Calculate totals, averages, grades, and pass/fail results."""
    # NumPy is used to calculate totals and averages from subject marks.
    marks_array = data[SUBJECTS].to_numpy()
    data["Total_Marks"] = np.sum(marks_array, axis=1)
    data["Average_Marks"] = np.round(np.mean(marks_array, axis=1), 2)

    # Use a loop to assign grade and pass/fail status to every student.
    grades = []
    results = []
    for _, student in data.iterrows():
        grades.append(assign_grade(student["Average_Marks"]))
        results.append(check_pass_fail(student))

    data["Grade"] = grades
    data["Result"] = results
    return data


def show_student_results(data):
    """Display the student-wise result table."""
    print("\nSTUDENT-WISE RESULTS")
    print("-" * 105)
    columns_to_show = [
        "Student_ID", "Name", "Department", "Total_Marks",
        "Average_Marks", "Grade", "Result", "Attendance_Percent"
    ]
    print(data[columns_to_show].to_string(index=False))


def show_class_summary(data):
    """Display overall class statistics."""
    print("\nCLASS SUMMARY")
    print("-" * 40)
    print(f"Number of students : {len(data)}")
    print(f"Class average      : {data['Average_Marks'].mean():.2f}")
    print(f"Highest average    : {data['Average_Marks'].max():.2f}")
    print(f"Lowest average     : {data['Average_Marks'].min():.2f}")
    print(f"Students passed    : {(data['Result'] == 'Pass').sum()}")
    print(f"Students failed    : {(data['Result'] == 'Fail').sum()}")
    print(f"Average attendance : {data['Attendance_Percent'].mean():.2f}%")


def show_subject_analysis(data):
    """Show average marks for each subject and identify the best subject."""
    subject_averages = data[SUBJECTS].mean().round(2)
    print("\nSUBJECT-WISE AVERAGE MARKS")
    print("-" * 40)
    for subject, average in subject_averages.items():
        print(f"{subject:20s}: {average:.2f}")

    best_subject = subject_averages.idxmax()
    lowest_subject = subject_averages.idxmin()
    print(f"\nBest-performing subject  : {best_subject} ({subject_averages[best_subject]:.2f})")
    print(f"Lowest-average subject   : {lowest_subject} ({subject_averages[lowest_subject]:.2f})")


def show_top_performers(data, number=3):
    """Display the top students according to average marks."""
    top_students = data.sort_values(
        by=["Average_Marks", "Name"], ascending=[False, True]
    ).head(number)

    print(f"\nTOP {number} PERFORMING STUDENTS")
    print("-" * 55)
    print(top_students[["Student_ID", "Name", "Average_Marks", "Grade"]].to_string(index=False))


def main():
    """Run all project steps in order."""
    print("=" * 60)
    print("       STUDENT PERFORMANCE ANALYTICS SYSTEM")
    print("=" * 60)

    data = load_student_data(DATA_FILE)
    if data is None:
        return

    print(f"\nDataset loaded successfully: {len(data)} student records.")
    print("Departments found:", ", ".join(sorted(data["Department"].unique())))

    data = analyze_students(data)
    show_student_results(data)
    show_class_summary(data)
    show_subject_analysis(data)
    show_top_performers(data)

    # Save the analysis results to a new CSV file for later viewing.
    output_file = "student_analysis_results.csv"
    data.to_csv(output_file, index=False)
    print(f"\nAnalysis results saved to: {output_file}")
    print("\nAnalysis completed successfully!")


if __name__ == "__main__":
    main()
