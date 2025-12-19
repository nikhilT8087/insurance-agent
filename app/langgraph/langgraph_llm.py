from langchain_core.language_models import BaseChatModel
from langchain_core.messages import HumanMessage, AIMessage
from typing import List

from app.langgraph.graph import insurance_graph
from app.langgraph.state import ConversationState


class LangGraphChatModel(BaseChatModel):
    def __init__(self, call_id: str):
        self.state = ConversationState(call_id=call_id)

    @property
    def _llm_type(self):
        return "langgraph"

    def _generate(self, messages: List, **kwargs):
        last_user = next(
            m.content for m in reversed(messages)
            if isinstance(m, HumanMessage)
        )

        self.state.last_user_message = last_user
        self.state = insurance_graph.invoke(self.state)

        return AIMessage(content=self.state.response or "")
