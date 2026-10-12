from llm import get_llm
from retriever import retrieve_documents


def answer_question(question: str):

    documents = retrieve_documents(question)

    context = "\n\n".join(
        document.page_content
        for document in documents
    )

    prompt = f"""
You are an enterprise sales analyst.

Answer the user's question using ONLY the
provided context.

If the context does not contain enough information,
say that there is insufficient evidence.

Do not invent facts.

Context:
{context}

Question:
{question}

Answer:
"""

    llm = get_llm()

    response = llm.invoke(prompt)

    return response.content