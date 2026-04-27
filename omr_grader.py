import pandas as pd
import os

ANSWER_KEY_PATH = "answer_key.xlsx"
STUDENT_FOLDER = "studentanswers"
OUTPUT_FOLDER = "output"
NUM_QUESTIONS = 20

correct_answers = dict(pd.read_excel(ANSWER_KEY_PATH).values)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

for filename in os.listdir(STUDENT_FOLDER):
    if filename.endswith(".xlsx"):
        filepath = os.path.join(STUDENT_FOLDER, filename)
        try:
            df = pd.read_excel(filepath)
            if 'Question' not in df or 'Answer' not in df:
                print(f"Skipped: {filename} (missing columns)")
                continue

            student_answers = dict(df[['Question', 'Answer']].values)
            rows = []
            score = 0

            for q in range(1, NUM_QUESTIONS + 1):
                sa = student_answers.get(q, "").strip().lower()
                ca = correct_answers.get(q, "").strip().lower()
                correct = sa == ca
                if correct:
                    score += 1
                rows.append([q, sa.upper(), ca.upper(), correct])

            rows.append(["Total", "", "", f"{score}/{NUM_QUESTIONS}"])

            pd.DataFrame(rows, columns=["Question", "StudentAnswer", "CorrectAnswer", "IsCorrect"])\
              .to_excel(os.path.join(OUTPUT_FOLDER, f"{os.path.splitext(filename)[0]}_graded.xlsx"), index=False)

        except:
            print(f"Error in: {filename}")

print("Grading complete.")