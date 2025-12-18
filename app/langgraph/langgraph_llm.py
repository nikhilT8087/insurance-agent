from typing import List
from langchain_core.messages import AIMessage, HumanMessage, BaseMessage
from langchain_core.language_models import BaseChatModel

from app.langgraph.graph import insurance_graph
from app.langgraph.state import ConversationState