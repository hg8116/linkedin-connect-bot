# LinkedIn Connect Bot

This bot automates sending connection requests and following users on LinkedIn using Python and Selenium.

## Prerequisites

- Python 3.x
- [Firefox](https://www.mozilla.org/en-US/firefox/new/)

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

## Notes

1. Ensure you have Firefox installed as the Selenium driver is set to use Firefox.

2. Modify the `linkedin-links.ods` file or add your own to include the LinkedIn profile URLs you want to connect with or follow.

3. This bot will attempt to send a connection request to each LinkedIn URL. If it can't send a connection request, it will try to follow the user instead.

## Disclaimer

Use this bot responsibly and in accordance with LinkedIn's terms of service. Automating actions on LinkedIn can lead to your account being restricted or banned if not used carefully.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.
