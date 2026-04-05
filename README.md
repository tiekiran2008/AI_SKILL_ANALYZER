🚀 AI Skill Analyzer
📌 Overview

AI Skill Analyzer is a Python-based project that analyzes student/intern performance data and generates intelligent feedback using AI. It processes CSV data, identifies trends, and produces a structured JSON report.

🎯 Features
->📊 Data analysis using pandas
->📈 Identifies strengths & weaknesses
->🤖 AI-generated feedback (Gemini API)
->📄 JSON report output

🛠️ Tech Stack
->Python
->Pandas
->Gemini API
->JSON

📁 Project Structure
</> Bash
AI_Skill_Analyzer/
├── mock_data.csv
├── processor.py
├── ai_engine.py
├── main.py
├── skill_report.json

▶️ How to Run
</> Bash
python -m venv venv
venv\Scripts\activate
pip install pandas google-generativeai
python main.py

📄 Output
Generates:
 skill_report.json

Contains:
->Performance metrics
->Insights
->AI-generated summary

👨‍💻 Author
->Kiran Kumar

⭐ Note
->Do not share your API key publicly.
