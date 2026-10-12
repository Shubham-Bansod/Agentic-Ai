from planner import plan_queries


question = "Why did Maharashtra sales decrease last quarter?"

queries = plan_queries(question)

print("\nGenerated queries:\n")

for i, query in enumerate(queries, start=1):
    print(f"{i}. {query}")