from vectorstore import create_vectorstore


def retrieve_documents(query: str, k: int = 3):

    vectorstore = create_vectorstore()

    retriever = vectorstore.as_retriever(
        search_kwargs={
            "k": k
        }
    )

    documents = retriever.invoke(query)

    return documents