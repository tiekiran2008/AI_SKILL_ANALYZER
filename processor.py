import pandas as pd

def analyze_performance(csv_file):
    """
    Reads CSV file and analyzes performance.
    Returns statistics and trends.
    """
    df = pd.read_csv(csv_file)

    # Calculate average score and time per topic
    summary = df.groupby('topic').agg({
        'score': 'mean',
        'time_taken': 'mean'
    }).to_dict('index')

  
    trends = []

    for topic, data in summary.items():
        if data['score'] > 90:
            trends.append(f"Strong performance in {topic}")
        elif data['score'] < 65:
            trends.append(f"Needs improvement in {topic}")

        if data['time_taken'] > 70:
            trends.append(f"Taking more time on {topic}")

    return {
        "stats": summary,
        "trends": trends
    }