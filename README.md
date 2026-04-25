# 📝 Automated OMR Sheet Grading System

> Python-based automation that reads student answer sheets, compares with an answer key, and generates graded results — eliminating manual checking.

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white)
![Excel](https://img.shields.io/badge/Excel-217346?style=flat-square&logo=microsoftexcel&logoColor=white)

---

## 📌 Project Overview

This project applies **Robotic Process Automation (RPA)** concepts to academic evaluation. The system reads multiple student Excel sheets, compares answers against an answer key, calculates scores, and outputs graded results — all automatically.

---

## ✨ Features

- Processes **multiple student files** in a single run
- Compares answers against a predefined answer key
- Calculates score per student
- Outputs structured, individual graded Excel files
- Error handling for missing or invalid data

---

## 🔄 Workflow

```
Student Answer Files (Excel) 
        ↓
Python Script (reads + compares)
        ↓
Answer Key File
        ↓
Score Calculation
        ↓
Graded Output Files (per student)
```

---

## 🗂️ Project Structure

```
omr-sheet-grading/
│
├── input/
│   ├── answer_key.xlsx            # Correct answers
│   └── students/
│       ├── student_001.xlsx
│       ├── student_002.xlsx
│       └── ...
│
├── output/
│   └── graded/                    # Auto-generated graded files
│
├── grader.py                      # Main grading script
├── requirements.txt
└── README.md
```

---

## 🚀 How to Run

```bash
git clone https://github.com/krishas-7/omr-sheet-grading.git
cd omr-sheet-grading
pip install -r requirements.txt

# Place student files in input/students/
# Place answer key in input/answer_key.xlsx

python grader.py
# Graded files appear in output/graded/
```

---

## 📦 Requirements

```
pandas
openpyxl
```

---

## 💡 Key Concepts Demonstrated

- File I/O and automation in Python
- Pandas for data comparison and manipulation
- RPA-style batch processing
- Structured output generation

---

*Built by [Krisha Shah](https://www.linkedin.com/in/krishas7) · Mumbai, India*
