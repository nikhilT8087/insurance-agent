from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from app.langgraph.state import ConversationState

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

prompt = ChatPromptTemplate.from_template("""
        Classify the user as:
        - existing_customer
        - new_customer
        
        Message: {message}
        
        Return only the classification.
    """)

def identify_node(state: ConversationState):
    """
        This function analyzes the user’s latest message to classify them as either an existing customer or a new customer.
        It uses an LLM-based prompt chain to perform the classification, updates the conversation state by setting the
        `is_existing_customer` flag accordingly, and returns the updated conversation state.

        :param state: ConversationState object containing the latest user message and conversation context.
        :return: Updated ConversationState with the `is_existing_customer` flag set based on the classification result.
    """

    chain = prompt | llm | StrOutputParser()
    result = chain.invoke({"message": state.last_user_message})
    state.is_existing_customer = result == "existing_customer"
    return state
