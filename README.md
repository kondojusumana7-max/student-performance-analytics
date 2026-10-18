# Student Performance Analytics System

A beginner-friendly Python data-analysis project for the Python with AI internship assignment. It uses Python, NumPy, and Pandas to summarize student marks and attendance.

## Features
- Reads 20 sample student records from `students.csv` using Pandas.
- Uses NumPy to calculate each student's total and average marks.
- Assigns grades using a clearly defined grading scale.
- Marks a student as Pass only when every subject mark is at least 35.
- Displays highest, lowest, and class-average performance.
- Calculates subject-wise averages and identifies the highest/lowest-average subjects.
- Lists the top 3 students by average marks.
- Saves calculated results to `student_analysis_results.csv`.

## Files
- `main.py` — main program.
- `students.csv` — sample dataset with 20 fictional student records.
- `Project_Documentation.md` — project report.
- `requirements.txt` — required Python libraries.

## Requirements
- Python 3.9 or later recommended.
- Pandas
- NumPy

## How to run
1. Install Python from https://www.python.org/downloads/ if it is not already installed.
2. Open a terminal/command prompt in this project folder.
3. Install dependencies:
   ```bash
   python -m pip install -r requirements.txt
   ```
4. Run:
   ```bash
   python main.py
   ```
   On some Windows computers, use `py main.py` instead of `python main.py`.
5. Check the terminal output and the generated `student_analysis_results.csv` file.

## Grading rules
- A+: average >= 90
- A: average >= 80 and < 90
- B: average >= 70 and < 80
- C: average >= 60 and < 70
- D: average >= 50 and < 60
- F: average < 50

Pass/fail is separate from grade: a student passes only if every subject score is at least 35. The dataset is fictional and intended for learning only.

## GitHub
Create a public repository named `student-performance-analytics` (unless your trainer specifies a different visibility setting), upload the project files, and copy the repository URL into the internship submission form.
