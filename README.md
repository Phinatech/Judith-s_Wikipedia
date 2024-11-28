# Random Wikipedia Article Fetcher
This is a simple Python-based application that fetches random articles from Wikipedia using its API. Users can view the title, summary, and a link to the full article and optionally open the full article in their browser.



# bash
git clone https://github.com/Phinatech/Judith-s_Wikipedia.git
cd random-wikipedia-fetcher


# bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Add your API URL: = "https://en.wikipedia.org/api/rest_v1/page/random/summary"

# Create a file named config.py in the root directory.
Add the following line:
python
Copy code
API_URL = "https://en.wikipedia.org/api/rest_v1/page/random/summary"
Running the Application Locally

# Open a terminal and navigate to the project directory.
# Run the application:
bash
Copy code
python index.py
Follow the on-screen instructions to fetch random Wikipedia articles.

# Deploying to Web Servers
this is the deployed link 
deployed link: https://www.phinatechlive.tech



# Use the provided URL to access your application.
APIs Used
Wikipedia API:
Endpoint: https://en.wikipedia.org/api/rest_v1/page/random/summary
Documentation: Wikipedia REST API Docs

# video link
https://www.loom.com/share/ae94f532b90d4c94a8b1ed34838ebf4c

# Project Structure
bash
Copy code
random-wikipedia-fetcher/
├── index.py            # Main application logic
├── config.py          # Configuration file (not tracked by Git)  
├── README.md          # Documentation
└── .gitignore         # Git ignore file
Contributions
Contributions are welcome! Please fork the repository, create a new branch, and submit a pull request with your changes.

# License
This project is licensed under the MIT License. See LICENSE for more details.

Let me know if you have further questions or need additional deployment instructions! 🚀








