def sentiment_agent(state, llm):
    prompt = f"""
    You are a culinary quality expert.

    From this review summary:
    {state['review_summary']}

    Identify:
    • Overall sentiment (positive/neutral/negative)
    • Specific FOOD issues (taste, salt, oil, spice, texture, dryness, freshness,etc)

    Ignore service, hygiene, or restaurant operations.

    Respond in 2–3 short bullet points.
    """
    return {"sentiment_insights": llm.invoke(prompt)}