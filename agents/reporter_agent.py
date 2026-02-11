def reporter_agent(state, llm):
    prompt = f"""
    Final Kitchen Report for {state['recipe_name']}:

    {state['improvement_advice']}

    Present in 2 professional bullet points.
    """

    return {"final_report": llm.invoke(prompt)}
