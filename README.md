# TikTok Trends Flask App

This Flask app allows users to explore TikTok trends and find videos based on their specific criteria. It integrates with the OpenAI API to provide conversational assistance in gathering user preferences and retrieving relevant TikTok data.

## Features

- **Initiate Conversation**: Welcomes users and explains how the app can help them explore TikTok trends.
- **Gather User Input**: Asks users a series of questions to collect their TikTok search criteria.
- **Validate Input**: Ensures user input matches the expected format and provides feedback if needed.
- **Execute Function**: Calls the appropriate function to fetch TikTok data based on user preferences.
- **Display Results**: Presents the retrieved TikTok data to users in a clear and organized manner.
- **Follow-up**: Offers further assistance to users, such as refining their search criteria.

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
