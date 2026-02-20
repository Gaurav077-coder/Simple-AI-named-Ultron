from openai import OpenAI

client = OpenAI(api_key="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")

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a virtual assistant named Friday."},
        {"role": "user", "content": "What is programming?"}
    ]
)

print(response.choices[0].message.content)