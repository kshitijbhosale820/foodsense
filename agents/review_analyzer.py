def review_analyzer_agent(state, llm):
    reviews = [str(r) for r in state["reviews"] if isinstance(r, str)]
    combined_reviews = " ".join(reviews)[:1500]

    prompt = f"""
    Analyze customer feedback and return TWO things:

    1. Overall sentiment: Positive / Mixed / Negative
    2. Key food-related issues (if any)

    Reviews:
    {combined_reviews}

    Keep response under 50 words.
    """

    return {"review_summary": llm.invoke(prompt)}
