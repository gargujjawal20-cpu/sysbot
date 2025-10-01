# SysBot - AI System Status Assistant

A simple, command-line chatbot that uses the Google Gemini API to answer questions about your computer's system status in natural language.

## Features

-   **Real-time System Info:** Provides live data on CPU usage, memory, battery status, and network information.
-   **Natural Language Interface:** Ask questions like "What's my CPU usage?" or "How is my memory doing?" instead of running terminal commands.
-   **Powered by Gemini:** Leverages the power of Google's Gemini Pro model to understand questions and formulate clear, concise answers.
-   **Extensible:** Easily add new system information functions to expand the bot's knowledge.

## Setup and Installation

Follow these steps to get SysBot running on your local machine.

### 1. Prerequisites

-   Python 3.8 or newer
-   A Google AI Studio API Key

### 2. Installation Steps

1.  **Clone or create the project directory:**
    ```sh
    mkdir sysbot
    cd sysbot
    ```

2.  **Create a virtual environment (recommended):**
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Create a `requirements.txt` file** with the following content:
    ```txt
    google-generativeai
    python-dotenv
    psutil
    ```

4.  **Install the dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

5.  **Create a `.env` file** in the project root to store your API key:
    ```
    GOOGLE_API_KEY="YOUR_API_KEY_HERE"
    ```

6.  **Create the Python files:** You will need three files: `main.py`, `chatbot.py`, and `system_info.py`. Make sure they are in the same directory.

## Usage

Once everything is set up, run the main application from your terminal:

```sh
python main.py