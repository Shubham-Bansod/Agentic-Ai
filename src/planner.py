from pydantic import BaseModel, Field
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv


class QueryPlan(BaseModel):

    queries: list[str] = Field(
        description="Search queries needed to answer the user's question"
    )
load_dotenv()


def get_planner():

    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0
    )

    return llm.with_structured_output(QueryPlan)


def plan_queries(question: str) -> list[str]:

    planner = get_planner()

    prompt = f"""
You are a query planning agent for an enterprise sales
analytics RAG system.

Break the user's question into multiple focused search
queries.

Each query should retrieve a different piece of evidence
needed to answer the original question.

Avoid duplicate queries.

User question:

{question}
"""

    result = planner.invoke(prompt)

    return result.queries