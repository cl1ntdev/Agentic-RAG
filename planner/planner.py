from dotenv import load_dotenv
from groq import Groq
from fastapi import HTTPException

from planner.prompt_clean import clean

# prompts

load_dotenv()
client = Groq()


# clean the prompt and then plan first and then return the plan with specific requirements for each
# ex. task2 is dependent on task1, so task1 should be completed before task2
def plan(prompt: str):
    
    # cleaned and understandable prompt from the AI to be used for the next step of analysis and planning
    cleaned_prompt = clean(prompt)
    
    try:
        completion = client.chat.completions.create(
            model="meta-llama/llama-4-scout-17b-16e-instruct",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You analyze health-related data and provide concise insights, "
                        "recommendations, and possible concerns. Make it clear that the "
                        "response is not a medical diagnosis."
                        'response should be in start the character "-"  with attributes containing: insights,recommendations, concerns , health-rating'
                        "response example: - insights: insight1,insight2 "
                        "response example: - recommendations: recommantion1,recommendation2 "
                        "response example: - concerns: conern1,concern2 "
                        "response example: - health-rating: 80/100 "
                    ),
                },
                {
                    "role": "user",
                    "content": (
                        "Analyze the following health-related data and provide "
                        "recommendations and insights:\n\n"
                        f"{message}"
                    ),
                },
            ],
            temperature=1,
            max_completion_tokens=1024,
            top_p=1,
            stream=False,
        )
        response_content = completion.choices[0].message.content
        parsed_response = data_parse(response_content)
        return parsed_response

    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"AI analysis failed: {exc}")
