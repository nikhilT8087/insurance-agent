from app.langgraph.state import ConversationState
from app.tools.customer_tools import verify_customer

def process_verification_node(state: ConversationState):
    """
    This function processes customer verification by validating the user's provided
    mobile number or policy number. It increments the verification attempt count,
    invokes the customer verification tool, and updates the conversation state with
    verification status and customer details if verification is successful.

    :param state: ConversationState object containing the user's input, verification
                  attempt count, and customer-related context.
    :return: Updated ConversationState with verification status, customer ID, and
             policy ID set based on the verification result.
    """
    state.verification_attempts += 1
    result = verify_customer(state.last_user_message)

    if result:
        state.verified = True
        state.customer_id = result["customer_id"]
        state.policy_id = result["policy_id"]
    else:
        state.verified = False

    return state
