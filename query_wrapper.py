import sys
import embed

def main():
    if len(sys.argv) < 2:
        print("Error: Question required")
        return
    
    question = sys.argv[1]
    chunks = embed.query_db(question)
    prompt = "Please answer user's question according to context\n"
    prompt += f"Question: {question}\n"
    prompt += "Context:\n"
    for c in chunks:
        prompt += f"{c}\n"
        prompt += "-------------\n"
    
    result = embed.google_client.models.generate_content(
        model=embed.LLM_MODEL,
        contents=prompt
    )
    print(result.text)

if __name__ == '__main__':
    main()
