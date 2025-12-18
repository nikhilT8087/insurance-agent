from app.langgraph.state import ConversationState

def greeting_node(state: ConversationState):
    """
    This function sets a welcome message in the conversation state to greet the user on behalf of
    ABC Insurance and prompts them to identify whether they are an existing or new customer.
    It then returns the updated conversation state.

    :param state: ConversationState object that holds the current conversation context and response.
    :return: Updated ConversationState with the greeting message set.
    """
    state.response = (
        "Welcome to ABC Insurance. "
        "Are you an existing customer or a new customer?"
    )
    return state