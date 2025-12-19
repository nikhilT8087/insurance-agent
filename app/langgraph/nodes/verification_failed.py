from app.langgraph.state import ConversationState

def verification_failed_node(state: ConversationState):
    """
    This function handles failed customer verification by setting an appropriate
    response message prompting the user to retry providing their verification details.

    :param state: ConversationState object containing the current conversation context.
    :return: Updated ConversationState with a failure message set as the response.
    """
    state.response = (
        "I’m sorry, I couldn’t verify those details. "
        "Could you please try again?"
    )
    return state
