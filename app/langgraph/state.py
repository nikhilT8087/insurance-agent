from pydantic import BaseModel
from typing import Optional


class ConversationState(BaseModel):
    call_id: str

    # identity
    is_existing_customer: Optional[bool] = None
    verified: bool = False
    verification_attempts: int = 0

    customer_id: Optional[str] = None
    policy_id: Optional[str] = None

    # conversation
    last_user_message: Optional[str] = None
    intent: Optional[str] = None

    # agent output
    response: Optional[str] = None
