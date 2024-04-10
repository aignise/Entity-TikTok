import os
from dotenv import load_dotenv
from entity import create_thread, start, get_response

load_dotenv()

def main():
    while True:
        prompt = input("Please provide the job preference you wish to search for: ")
        assistant_id = os.getenv("ASSISTANT_ID")
        thread_id = create_thread()
        start(thread_id, prompt)
        response = get_response(thread_id, assistant_id)
        print(response)
    
        while True:
            further_assistance = input("Do you need further assistance? (yes/no): ").lower()
            if further_assistance in ["yes", "no"]:
                if further_assistance == "yes":
                    assistance_type = input("What type of assistance do you require? (job search/general): ").lower()
                    if assistance_type == "job search":
                        # Rerun job search
                        prompt = input("Please provide the job preference you wish to search for: ")
                        start(thread_id, prompt)
                        response = get_response(thread_id, assistant_id)
                        print(response)
                        continue
                    elif assistance_type == "general":
                        # Provide general assistance
                        next_query = input("How can I help you? ")
                        start(thread_id, next_query)
                        response = get_response(thread_id, assistant_id)
                        print("Response:", response)
                        continue
                    else:
                        print("Invalid input. Please enter 'job search' or 'general'.")
                elif further_assistance == "no":
                    print("Thank you for using the assistant. Goodbye!")
                break
            else:
                print("Please enter 'yes' or 'no'.")
        break
if __name__ == "__main__":
    main()
