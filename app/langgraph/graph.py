from langgraph.graph import StateGraph, END
from app.langgraph.state import ConversationState

from app.langgraph.nodes.greeting import greeting_node
from app.langgraph.nodes.identify import identify_node
from app.langgraph.nodes.ask_verification import ask_verification_node
from app.langgraph.nodes.process_verification import process_verification_node
from app.langgraph.nodes.verification_failed import verification_failed_node
from app.langgraph.nodes.post_verify import post_verify_node

graph = StateGraph(ConversationState)

graph.add_node("greeting", greeting_node)
graph.add_node("identify", identify_node)
graph.add_node("ask_verification", ask_verification_node)
graph.add_node("process_verification", process_verification_node)
graph.add_node("verification_failed", verification_failed_node)
graph.add_node("post_verify", post_verify_node)

graph.set_entry_point("greeting")

graph.add_edge("greeting", "identify")

graph.add_conditional_edges(
    "identify",
    lambda s: "ask_verification" if s.is_existing_customer else "post_verify"
)

graph.add_edge("ask_verification", "process_verification")

graph.add_conditional_edges(
    "process_verification",
    lambda s: "post_verify" if s.verified else "verification_failed"
)

graph.add_conditional_edges(
    "verification_failed",
    lambda s: END if s.verification_attempts >= 2 else "ask_verification"
)

graph.add_edge("post_verify", END)

insurance_graph = graph.compile()
