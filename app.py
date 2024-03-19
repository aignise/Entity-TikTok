from flask import Flask, request, jsonify
import openai
import requests
import json
from dotenv import load_dotenv
import os
import time

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

# Initialize the OpenAI client
client = openai.OpenAI(api_key=openai_api_key)

app = Flask(__name__)

def setup():
    assistant = client.beta.assistants.create(
        name="TikTok Trends Fetch",
        instructions="You are a bot to fetch TikTok trends based on user preferences.",
        model="gpt-4-turbo-preview",  # Assuming this is suitable for TikTok trends
        tools=[
            {
                "type": "function",
                "function": {
                    "name": "fetch_tiktok_data",
                    "description": "Fetches TikTok trends based on user preferences.",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "region": {
                                "type": "string",
                                "description": "Region code (e.g., us)"
                            },
                            "count": {
                                "type": "integer",
                                "description": "Number of trends to fetch"
                            }
                        },
                        "required": ["region", "count"]
                    }
                }
            }
        ]
    )

    return assistant.id

def fetch_tiktok_data(region="us", count=10):
    # TikTok data retrieval code
    url = "https://tiktok-scraper7.p.rapidapi.com/feed/list"
    querystring = {"region": region, "count": count}
    headers = {
        "X-RapidAPI-Key": os.getenv("X_RAPIDAPI_KEY"),
        "X-RapidAPI-Host": "tiktok-scraper7.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None

def create_thread():
    """Creates a thread for conversation."""
    thread = client.beta.threads.create()
    return thread.id

def start(thread_id, user_query):
    """Starts a conversation in the specified thread with the given user query."""
    message = client.beta.threads.messages.create(
        thread_id=thread_id,
        role="user",
        content=user_query
    )
    
def get_response(thread_id, assistant_id, user_query):
    """Retrieves the response from the OpenAI API."""
    run = client.beta.threads.runs.create(
        thread_id=thread_id,
        assistant_id=assistant_id,
        instructions="Answer user questions using custom functions available to you."
    )
    
    while True:
        run_status = client.beta.threads.runs.retrieve(thread_id=thread_id, run_id=run.id)
        if run_status.status == "completed":
            break
        elif run_status.status == 'requires_action':
            submit_tool_outputs(thread_id, run.id, run_status, user_query)
        
        time.sleep(1)
    
    messages = client.beta.threads.messages.list(thread_id=thread_id)
    response = messages.data[0].content[0].text.value
    return response

def submit_tool_outputs(thread_id, run_id, run_status, user_query):
    """Submits tool outputs to the OpenAI API."""
    output = fetch_tiktok_data(region="us", count=10)  # Fetch TikTok data
    output_str = json.dumps(output)
    
    tool_calls = run_status.required_action.submit_tool_outputs.tool_calls
    
    tool_outputs = []
    for tool_call in tool_calls:
        tool_outputs.append({
            "tool_call_id": tool_call.id,
            "output": output_str
        })
    
    # Submit tool outputs to OpenAI API
    client.beta.threads.runs.submit_tool_outputs(
        thread_id=thread_id,
        run_id=run_id,
        tool_outputs=tool_outputs
    )

@app.route('/fetch_tiktok_trends', methods=['POST'])
def fetch_tiktok_trends():
    user_query = request.json.get('user_query', '')
    assistant_id = os.getenv("OPENAI_ASSISTANT_ID")
    thread_id = create_thread()
    start(thread_id, user_query)
    response = get_response(thread_id, assistant_id, user_query)
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
