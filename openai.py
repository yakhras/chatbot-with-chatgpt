from openai import OpenAI

client = OpenAI(
  api_key="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"
)

completion = client.chat.completions.create(
  model="gpt-4o-mini",
  store=True,
  messages=[
    {"role": "user", "content": "write a haiku about ai"}
  ]
)

print(completion.choices[0].message)
