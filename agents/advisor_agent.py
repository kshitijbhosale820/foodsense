def advisor_agent(state, llm):

    prompt = f"""
    Dish: {state['recipe_name']}

    Review Analysis:
    {state['review_summary']}

    RULES:
    - If sentiment is POSITIVE and no major issue → say dish is performing well and only suggest monitoring consistency.
    - If MIXED → suggest small improvements.
    - If NEGATIVE → suggest clear cooking improvements.

    Give 2 short bullet points only.
    Focus ONLY on recipe quality, not service or marketing.
    """

    return {"improvement_advice": llm.invoke(prompt)}
