from retriever import src                                                                                                                                                                         retrieve_documents


query = "Why did Maharashtra sales decrease?"

documents = retrieve_documents(query)


print("\nRetrieved Documents:\n")

for i, doc in enumerate(documents, start=1):

    print(f"--- Document {i} ---")

    print("Source:", doc.metadata["source"])

    print(doc.page_content)

    print()