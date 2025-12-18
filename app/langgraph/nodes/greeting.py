from app.langgraph.state import ConversationState

def greeting_node(state: ConversationState):
    state.response = (
        "Welcome to ABC Insurance. "
        "Are you an existing customer or a new customer?"
    )
    return state