from rag import answer_question


question = input("Ask a question: ")

answer = answer_question(question)

print("\nAnswer:")
print(answer)