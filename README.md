# YouTube Video Transcript Fetcher
This basic project allows you to fetch the latest videos from a Youtube user, get some basic details, and the transcript.

It utilizes the YouTube Data API and `youtube-transcript-api` library to achieve this functionality.

## Features

- Fetch the latest videos from a specified YouTube user within the past 24 hours.
- Retrieve video details such as title and description.
- Retrieve video transcripts in both structured and plain text formats.

## Requirements

- Python 3.x
- A YouTube Data API key

## Installation

1. **Clone the repository**

    ```sh
    git clone <repository-url>
    cd <repository-directory>
    ```

2. **Create a virtual environment**

    ```sh
    python -m venv venv
    ```

3. **Activate the virtual environment**

    For Unix or MacOS:
    ```sh
    source venv/bin/activate
    ```


4. **Install the required packages**

    ```sh
    pip install -r requirements.txt
    ```

5. **Run the script**

    ```sh
    python main.py
    ```
