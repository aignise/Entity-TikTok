# TikTok Trends Flask App

This Flask app allows users to explore TikTok trends and find videos based on their specific criteria. It integrates with the OpenAI API to provide conversational assistance in gathering user preferences and retrieving relevant TikTok data.

## Features

- **Initiate Conversation**: Welcomes users and explains how the app can help them explore TikTok trends.
- **Gather User Input**: Asks users a series of questions to collect their TikTok search criteria.
- **Validate Input**: Ensures user input matches the expected format and provides feedback if needed.
- **Execute Function**: Calls the appropriate function to fetch TikTok data based on user preferences.
- **Display Results**: Presents the retrieved TikTok data to users in a clear and organized manner.
- **Follow-up**: Offers further assistance to users, such as refining their search criteria.

# Setting Up OpenAI Assistant Using OpenAI API

Follow these steps to set up your OpenAI assistant using the OpenAI API:

1. **Sign Up for OpenAI API**:
   - Visit the OpenAI website and sign up for an account if you haven't already.
   - Subscribe to the OpenAI API plan that suits your needs.

2. **Get API Key**:
   - Once subscribed, you'll receive an API key. This key is essential for authenticating your requests.

3. **Install OpenAI Python Library**:
   - Use pip to install the OpenAI Python library:
     ```
     pip install openai
     ```

4. **Import OpenAI Library**:
   - In your Python script or environment, import the OpenAI library:
     ```python
     import openai
     ```

5. **Set API Key**:
   - Set your API key using the `openai.api_key` attribute:
     ```python
     openai.api_key = 'YOUR_API_KEY'
     ```

6. **Invoke OpenAI API**:
   - Use the OpenAI API to interact with the language model. For example:
     ```python
     response = openai.Completion.create(
         engine="text-davinci-003",
         prompt="Once upon a time",
         max_tokens=50
     )
     print(response.choices[0].text.strip())
     ```

7. **Explore API Documentation**:
   - Refer to the official OpenAI API documentation for detailed information on endpoints, parameters, and usage examples.

8. **Understand API Usage and Billing**:
   - Familiarize yourself with usage limits and billing details to avoid exceeding quotas and unexpected charges.

9. **Experiment and Develop**:
   - Start experimenting with the OpenAI models, explore prompts, and develop your applications.

10. **Handle Errors and Exceptions**:
    - Implement error handling mechanisms in your code to gracefully handle any errors during API requests.

By following these steps, you can set up and start using the OpenAI API to interact with powerful language models and build innovative applications leveraging artificial intelligence capabilities.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your_username/tiktok-trends-flask-app.git
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Set up environment variables:

    - Create a `.env` file in the root directory.
    - Add your OpenAI API key and other necessary credentials:

        ```plaintext
        OPENAI_API_KEY=your_openai_api_key
        X_RAPIDAPI_KEY=your_rapidapi_key
        ```

4. Run the Flask app:

    ```bash
    python app.py
    ```

## Usage

- Access the app through the provided endpoint (`/tiktok`) using a POST request.
- Send a JSON object with the user query:

    ```json
    {
        "user_query": "Please provide your preferences for TikTok trends (e.g., region, count):"
    }
    ```

- The app will respond with TikTok data based on the user's preferences.

## Contributing

Contributions are welcome! Please feel free to submit issues and pull requests.

## License

This project is licensed under the [MIT License](LICENSE).
