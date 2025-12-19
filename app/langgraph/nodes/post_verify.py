from app.langgraph.state import ConversationState

def post_verify_node(state: ConversationState):
    """
    This function is executed after successful customer verification.
    It sets a confirmation message and prompts the user to state how they can be assisted.

    :param state: ConversationState object containing the verified customer context.
    :return: Updated ConversationState with a post-verification prompt set as the response.
    """
    state.response = "Thanks for confirming. How can I help you today?"
    return state
