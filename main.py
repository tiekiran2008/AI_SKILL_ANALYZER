from processor import analyze_performance
from ai_engine import get_ai_summary
import json

def generate_weekly_report():
    """
    Main function to run full pipeline.
    """
    print("Step 1: Reading and analyzing data...")
    results = analyze_performance("mock_data.csv")

    print("Step 2: Generating AI summary...")
    ai_summary = get_ai_summary(results)

    
    final_report = {
        "metrics": results["stats"],
        "insights": results["trends"],
        "dashboard_message": ai_summary
    }

    with open("skill_report.json", "w") as f:
        json.dump(final_report, f, indent=4)

    print("Report generated successfully!")

if __name__ == "__main__":
    generate_weekly_report()