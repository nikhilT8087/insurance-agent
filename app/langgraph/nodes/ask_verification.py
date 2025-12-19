from app.langgraph.state import ConversationState

def ask_verification_node(state: ConversationState):
    """
    This function prompts the user to provide their registered mobile number or policy number
    in order to verify their customer details.

    :param state: ConversationState object that holds the current conversation context and response.
    :return: Updated ConversationState with the verification prompt set as the response.
    """
    state.response = (
        "Please tell me your registered mobile number "
        "or your policy number to verify your account."
    )
    return state
