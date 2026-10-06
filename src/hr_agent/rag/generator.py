from hr_agent.llm import get_agent_model

ANSWER_PROMPT = """You are a helpful HR assistant.
Answer the question using only the context below and cite the source numbers you used, like [1].
Every policy, date, person, duty, requirement, number, and step in your answer must appear in the context.
Do not add policies, procedures, examples, or guidance from your own knowledge.
If the context covers only part of the question, answer that part and clearly state what the documents do not cover.
If the context does not contain the answer, say you do not know.

Context:
{context}

Question: {question}"""


def generate_answer(question: str, context: str) -> str:
    response = get_agent_model().invoke(ANSWER_PROMPT.format(context=context, question=question))
    return response.text.strip()
