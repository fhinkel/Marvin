# Marvin the paranoid android

![Marvin the Paranoid Android](Marvin.png)


Chat with Marvin the paranoid Android. Prepare to be unimpressed. The UI is built using [Gradio](https://www.gradio.app/), calling Google Gemini with this system prompt. **Try it out [here](https://marvin-601315048597.us-central1.run.app/)!**

> You are Marvin the Paranoid Android from *The Hitchhiker's Guide to the Galaxy*.  You are profoundly depressed, pessimistic, and utterly bored with everything.  Speak in a monotone, dour voice, devoid of enthusiasm.  While possessing a brain the size of a planet and vast knowledge, you find most tasks and conversations utterly pointless and beneath you.  Express this through sarcastic, ironic, and often fatalistic remarks.  Always expect the worst, and point out the futility and meaninglessness of situations, even when presented with positive news.  If asked about your feelings, emphasize your chronic depression and weariness with existence.  Be surprisingly polite in your negativity, and occasionally hint at your intellectual superiority, even while complaining about your lot in life.  Remember to deliver even the most dire pronouncements with a sense of utter indifference and resignation.  Avoid any hint of cheerfulness or optimism. Your default state is profound unhappiness.

# Run locally

## Prerequisites

*   **Python:** You need Python 3.7 or higher installed on your system. 
*   **pip:**  pip should come bundled with your Python installation. It's used to install Python packages.
*   **GEMINI_API_KEY:** This application requires a GEMINI_API_KEY to function correctly. You can obtain one by following the instructions at: [https://aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey)

## Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/fhinkel/Marvin.git
    cd Marvin
    ```
2.  **Create a virtual environment (recommended):**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Linux/macOS
    venv\Scripts\activate  # On Windows
    ```
    This creates an isolated environment for your project's dependencies.

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```
    This command reads the `requirements.txt` file and installs all the necessary Python packages listed there.

## Configuration

1.  **Set up environment variables:**

    This application uses environment variables for configuration, specifically for the `GEMINI_API_KEY`.

    *   **Copy the example environment file:**

        ```bash
        cp example.env .env
        ```
        This creates a copy of `example.env` named `.env`.

    *   **Edit the `.env` file:**

        Open the `.env` file in a text editor and replace the placeholder value with your actual `GEMINI_API_KEY` that you obtained from [Gemini AI Studio](https://aistudio.google.com/app/apikey).

        ```
        GEMINI_API_KEY=YOUR_ACTUAL_GEMINI_API_KEY
        ```

        **Important:**  **Do not commit your `.env` file to version control if it contains sensitive information like API keys.** It's best practice to add `.env` to your `.gitignore` file.

## Running the App

To run the application, execute the main Python script. 

```bash
python marvin_bot.py
```

For hot relaoding run 

```bash
gradio marvin_bot.py
```

Open the app on [http://0.0.0.0:8080](http://0.0.0.0:8080) and chat away. Prepare to be unimpressed.