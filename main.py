from fastapi import FastAPI
from brain.workerflow import start_workerflow


app = FastAPI()
# app.include_router(connection_router, prefix="/api")

@app.post('/user_prompt')
def user_prompt(prompt: str):
    response = start_workerflow(prompt)
    return {"message": f"Received prompt: {prompt}"}


def main():
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)