def get_ai_summary(data_results):
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=str(data_results)
        )
        return response.text
    except Exception as e:
        return "You are performing well overall. Focus more on improving weaker topics and managing time efficiently."