"""
EduPro – Standalone EDA Script
Prints all key analytical outputs to console.
"""
import pandas as pd
import warnings
warnings.filterwarnings("ignore")

# ── LOAD ──────────────────────────────────────
users        = pd.read_excel("data/users.xlsx", sheet_name="Users")
courses      = pd.read_excel("data/users.xlsx", sheet_name="Courses")
transactions = pd.read_excel("data/users.xlsx", sheet_name="Transactions")
teachers     = pd.read_excel("data/users.xlsx", sheet_name="Teachers")

# ── MERGE ─────────────────────────────────────
merged = (transactions
          .merge(users,   on="UserID")
          .merge(courses, on="CourseID")
          .merge(teachers, on="TeacherID", suffixes=("","_teacher")))

merged["TransactionDate"] = pd.to_datetime(merged["TransactionDate"])
bins   = [0, 17, 25, 35, 45, 100]
labels = ["<18", "18-25", "26-35", "36-45", "45+"]
merged["AgeGroup"] = pd.cut(merged["Age"], bins=bins, labels=labels)

print("=" * 60)
print("  EduPro – Key Performance Indicators")
print("=" * 60)
print(f"  Total Learners          : {users['UserID'].nunique():,}")
print(f"  Total Enrollments       : {transactions.shape[0]:,}")
print(f"  Avg Courses per Learner : {transactions.shape[0]/users['UserID'].nunique():.2f}")
print(f"  Total Courses Available : {courses.shape[0]}")
print(f"  Total Teachers          : {teachers.shape[0]}")
print(f"  Date Range              : {merged['TransactionDate'].min().date()} → {merged['TransactionDate'].max().date()}")

print("\n── Gender Distribution ─────────────────────────────")
print(users["Gender"].value_counts().to_string())

print("\n── Age Group Enrollment ────────────────────────────")
print(merged["AgeGroup"].value_counts().sort_index().to_string())

print("\n── Course Category Popularity ──────────────────────")
print(merged["CourseCategory"].value_counts().to_string())

print("\n── Course Level Preference ─────────────────────────")
print(merged["CourseLevel"].value_counts().to_string())

print("\n── Course Type (Paid vs Free) ──────────────────────")
print(merged["CourseType"].value_counts().to_string())

print("\n── Gender × Course Level ───────────────────────────")
print(pd.crosstab(merged["Gender"], merged["CourseLevel"]).to_string())

print("\n── Age Group × Course Category ─────────────────────")
pivot = pd.pivot_table(merged, values="TransactionID", index="AgeGroup",
                       columns="CourseCategory", aggfunc="count",
                       fill_value=0, observed=False)
print(pivot.to_string())

print("\n── Top 10 Courses ──────────────────────────────────")
print(merged["CourseName"].value_counts().head(10).to_string())

print("\n── Monthly Enrollment Volume ───────────────────────")
merged["Month"] = merged["TransactionDate"].dt.to_period("M").astype(str)
print(merged.groupby("Month").size().to_string())

print("\n── Top 10 Teachers by Enrollments ──────────────────")
t_counts = merged.groupby("TeacherName").size().reset_index(name="Enrollments")
print(t_counts.nlargest(10,"Enrollments").to_string(index=False))

print("\n" + "=" * 60)
print("  Analysis complete.")
print("=" * 60)
