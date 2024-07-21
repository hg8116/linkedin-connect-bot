# LinkedIn Connect Bot

This bot automates sending connection requests and following users on LinkedIn using Selenium.

## Setup

1. Clone the repository:

   ```sh
   git clone https://github.com/hg8116/linkedin-connect-bot.git
   cd linkedin-connect-bot
   ```

2. Create a virtual environment and activate it:

   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the dependencies:

   ```sh
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project directory and add your LinkedIn credentials:

   ```env
   LINKEDIN_USERNAME=your_username_here
   LINKEDIN_PASSWORD=your_password_here
   ```

5. Add your LinkedIn URLs to the .excel, .csv file or .ods file.

## Usage

Run the bot:

```sh
python linkedin_bot.py
```
