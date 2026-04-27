# 📝 Automated OMR Sheet Grading System

> Python-based RPA automation that reads 20 student answer sheets, compares with an answer key, and generates individual graded Excel reports — eliminating manual checking entirely.

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white)
![Excel](https://img.shields.io/badge/Excel-217346?style=flat-square&logo=microsoftexcel&logoColor=white)
![RPA](https://img.shields.io/badge/RPA-Automation-orange?style=flat-square)

---

## 📌 Project Overview

This project automates the grading of multiple-choice OMR answer sheets using Python. The script reads 20 student Excel files, compares each answer against a master answer key, calculates scores out of 20, and saves individual graded reports — all in a single run.

**From manual checking of 20 sheets → fully automated in seconds.**

---

## ✨ Features

- Processes **20 student answer sheets** in one run
- Compares answers against `answer_key.xlsx` (20 MCQ questions, A/B/C/D)
- Calculates score per student out of 20
- Outputs individual graded Excel per student with:
  - Question number
  - Student's answer
  - Correct answer
  - IsCorrect (TRUE/FALSE)
  - Total score at the bottom
- Skips invalid/missing files gracefully with error handling

---

## 📊 Sample Results

| Student | Score |
|---|---|
| student16 | 8/20 |
| student19 | 8/20 |
| student3 | 7/20 |
| student6 | 7/20 |
| student9 | 7/20 |
| student12 | 7/20 |
| student13 | 6/20 |
| student14 | 6/20 |
| student18 | 6/20 |
| student1 | 5/20 |
| student2 | 5/20 |
| student17 | 5/20 |
| student4 | 4/20 |
| student7 | 4/20 |
| student10 | 4/20 |
| student20 | 4/20 |
| student5 | 3/20 |
| student8 | 3/20 |
| student11 | 3/20 |
| student15 | 2/20 |

---

## 📋 Sample Graded Output (student1)

| Question | StudentAnswer | CorrectAnswer | IsCorrect |
|---|---|---|---|
| 1 | B | B | TRUE |
| 2 | C | B | FALSE |
| 3 | A | C | FALSE |
| ... | ... | ... | ... |
| Total | | | 5/20 |

---

## 🔄 Workflow

```
answer_key.xlsx (20 correct answers)
        +
studentanswers/ (student1.xlsx → student20.xlsx)
        ↓
omr_grader.py
        ↓
output/ (student1_graded.xlsx → student20_graded.xlsx)
```

---

## 🗂️ Project Structure

```
omr-sheet-grading/
│
├── omr_grader.py                  # Main grading script
├── answer_key.xlsx                # 20 correct answers (A/B/C/D)
│
├── studentanswers/                # Input — 20 student answer sheets
│   ├── student1.xlsx
│   ├── student2.xlsx
│   └── ... student20.xlsx
│
├── output/                        # Auto-generated after running script
│   ├── student1_graded.xlsx
│   └── ... student20_graded.xlsx
│
├── requirements.txt
└── README.md
```

---

## 🚀 How to Run

```bash
# Clone the repo
git clone https://github.com/krishas-7/omr-sheet-grading.git
cd omr-sheet-grading

# Install dependencies
pip install pandas openpyxl

# Run the grader
python omr_grader.py

# Graded files appear in output/ folder
```

---

## 📋 Input File Format

**answer_key.xlsx**
| Question | Correct Answer |
|---|---|
| 1 | b |
| 2 | b |
| 3 | c |
| ... | ... |
| 20 | a |

**student1.xlsx**
| Question | Answer |
|---|---|
| 1 | B |
| 2 | C |
| ... | ... |
| 20 | A |

---

## 💡 Key Concepts Demonstrated

- **RPA (Robotic Process Automation)** — automating repetitive manual tasks
- **Batch file processing** — looping through 20 files automatically
- **Pandas** for Excel read/write and data comparison
- **Error handling** — skips missing/malformed files without crashing
- **Structured output generation** — consistent graded report per student

---

## 📦 Requirements

```
pandas
openpyxl
```

---

*Built by [Krisha Shah](https://www.linkedin.com/in/krishas7) · Mumbai, India*
