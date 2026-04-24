from dotenv import load_dotenv
from fastapi import HTTPException
from groq import Groq

# prompts
from planner.prompts.cleaner.py import cleaner_prompt

load_dotenv()
client = Groq()



def clean(prompt: str):
    print("Cleaning the prompt...")
    try:
        completion = client.chat.completions.create(
            model="meta-llama/llama-4-scout-17b-16e-instruct",
            messages=[
                {
                    "role": "system",
                    "content": (cleaner_prompt),
                },
                {
                    "role": "user",
                    "content": (
                        "Analyze the following"
                        f"{prompt}"
                    ),
                },
            ],
            temperature=1,
            max_completion_tokens=1024,
            top_p=1,
            stream=False,
        )
        response_content = completion.choices[0].message.content
        return response_content
        # parsed_response = data_parse(response_content)
        # return parsed_response

    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"AI analysis failed: {exc}")
