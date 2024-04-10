import os
import time
import json
from dotenv import load_dotenv
from function import search_jobs
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def create_thread():
    thread = client.beta.threads.create()
    return thread.id

def start(thread_id , prompt):
    message = client.beta.threads.messages.create(
        thread_id=thread_id,
        role="user",
        content=prompt
    )

def get_response(thread_id, assistant_id):
    
    run = client.beta.threads.runs.create(
      thread_id=thread_id,
      assistant_id=assistant_id,
      instructions="Answer user questions using custom functions available to you."
    )
    
    # Wait for the run to complete
    run_status = client.beta.threads.runs.retrieve(thread_id=thread_id, run_id=run.id)
    while run_status.status != "completed":
        
        if run_status.status == 'requires_action':
            
            def get_outputs_for_tool_call(tool_call):
                if tool_call.function.name == "search_jobs":
                    query = json.loads(tool_call.function.arguments)["query"] 
                    output = search_jobs(query) 
                    output_str = json.dumps(output)
                    output_str = output_str[:1024 * 1024]
                return {
                    "tool_call_id":tool_call.id,
                    "output":output_str
                }
               
            tool_calls = run_status.required_action.submit_tool_outputs.tool_calls
            tool_outputs = map(get_outputs_for_tool_call, tool_calls)
            tool_outputs = list(tool_outputs)

            run = client.beta.threads.runs.submit_tool_outputs(
                thread_id=thread_id,
                run_id=run.id,
                tool_outputs=tool_outputs
            )

        time.sleep(1)
        run_status = client.beta.threads.runs.retrieve(thread_id=thread_id, run_id=run.id)

    # Retrieve the latest message from the thread
    
    messages = client.beta.threads.messages.list(thread_id=thread_id)
    response = messages.data[0].content[0].text.value
    return response


