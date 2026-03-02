from app.llm.system_prompt import SYSTEM_PROMPT


def build_prompt(user_query: str) -> str:
    return f"""
        {SYSTEM_PROMPT}
        User question: {user_query}
    """