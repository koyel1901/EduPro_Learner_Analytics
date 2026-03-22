# 📊 EduPro Learner Analytics Dashboard

**Unified Mentor × Toronto Government Parks, Forestry & Recreation**

A production-grade Streamlit dashboard for learner demographic and course enrollment behaviour analysis on the EduPro platform.

---

## 🗂 Project Structure

```
EduPro_Analytics/
├── app.py               ← Main Streamlit dashboard (5 analytical tabs)
├── analysis.py          ← Standalone CLI EDA script
├── data/
│   └── users.xlsx       ← Source data (4 sheets: Users, Courses, Transactions, Teachers)
├── assets/
│   ├── unified_mentor.png
│   └── toronto.png
├── requirements.txt
└── README.md
```

---

## 🚀 Quick Start

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Run the dashboard
```bash
streamlit run app.py
```

### 3. Run standalone analysis
```bash
python analysis.py
```

---

## 📋 Dataset Overview

| Sheet        | Rows  | Key Fields                                                         |
|--------------|-------|--------------------------------------------------------------------|
| Users        | 3,000 | UserID, UserName, Age, Gender, Email                               |
| Courses      | 60    | CourseID, CourseName, CourseCategory, CourseType, CourseLevel, CoursePrice, CourseRating |
| Transactions | 10,000| TransactionID, UserID, CourseID, TransactionDate, Amount, PaymentMethod, TeacherID |
| Teachers     | 60    | TeacherID, TeacherName, Age, Gender, Expertise, YearsOfExperience, TeacherRating |

---

## 📊 Dashboard Tabs

| Tab | Description |
|-----|-------------|
| 👥 Demographics | Age distribution, gender ratio, age × gender breakdowns |
| 📈 Enrollment Trends | Monthly trends, paid vs free, payment methods |
| 📚 Course Preferences | Category popularity, level distribution, top courses, category × level |
| 🔀 Segment Analysis | Age × category heatmap, gender × level, enrollment concentration |
| 🏫 Teacher Insights | Top teachers, rating distribution, rating vs enrollment scatter |

---

## 🎛 Filters (Sidebar)

- Age Group (`<18`, `18–25`, `26–35`)
- Gender (`Male`, `Female`)
- Course Category (12 categories)
- Course Level (`Beginner`, `Intermediate`, `Advanced`)
- Course Type (`Free`, `Paid`)

---

## 📦 Key KPIs

| KPI | Description |
|-----|-------------|
| Total Learners | Platform engagement indicator |
| Total Enrollments | Volume metric |
| Avg Courses / User | Engagement depth |
| Paid Enrollment % | Monetisation indicator |
| Avg Spend | Revenue per transaction |
| Top Category | Demand insight |

---

## 🏗 Tech Stack

- **Streamlit** — Web application framework
- **Pandas** — Data manipulation
- **Plotly** — Interactive visualisations
- **openpyxl** — Excel file I/O
