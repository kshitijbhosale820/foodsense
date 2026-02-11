from langgraph.graph import StateGraph, END
from agents.review_analyzer import review_analyzer_agent
from agents.sentiment_agent import sentiment_agent
from agents.advisor_agent import advisor_agent
from agents.reporter_agent import reporter_agent

def build_graph(llm, StateClass):
    workflow = StateGraph(StateClass)

    workflow.add_node("review_analyzer", lambda s: review_analyzer_agent(s, llm))
    workflow.add_node("sentiment", lambda s: sentiment_agent(s, llm))
    workflow.add_node("advisor", lambda s: advisor_agent(s, llm))
    workflow.add_node("reporter", lambda s: reporter_agent(s, llm))

    workflow.set_entry_point("review_analyzer")
    workflow.add_edge("review_analyzer", "sentiment")
    workflow.add_edge("sentiment", "advisor")
    workflow.add_edge("advisor", "reporter")
    workflow.add_edge("reporter", END)

    return workflow.compile()
