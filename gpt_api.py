import openai
openai.api_key = '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'
messages = []
while True:
	message = input(">")
	if message:
		messages.append(
			{"role": "user", "content": message},
		)
		chat = openai.ChatCompletion.create(
			model="gpt-4", messages=messages
		)
	reply = chat.choices[0].message.content
	print(f"ChatGPT: {reply}")
	messages.append({"role": "assistant", "content": reply})
