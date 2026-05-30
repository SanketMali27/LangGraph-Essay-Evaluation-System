from langgraph.graph import StateGraph
from langgraph.graph import START, END

from state import EssayState
from nodes import language_evaluator ,analysis_evaluator, clarity_evaluator, aggregator

workflow = StateGraph(EssayState)

workflow.add_node("language",language_evaluator)
workflow.add_node("analysis",analysis_evaluator)
workflow.add_node("clarity",clarity_evaluator)
workflow.add_node("aggregator",aggregator)


workflow.add_edge(START,"language")
workflow.add_edge(START,"analysis")
workflow.add_edge(START,"clarity")

workflow.add_edge( "language","aggregator")
workflow.add_edge("analysis","aggregator")
workflow.add_edge("clarity","aggregator")


workflow.add_edge("aggregator",END)

graph = workflow.compile()