
import requests
import webbrowser
try:
    from config import API_URL  
except ImportError:
    API_URL = None  

def fetch_random_article():
    if not API_URL:
        print("API URL is missing. Please add it to config.py.")
        return None

    response = requests.get(API_URL)
    if response.status_code == 200:
        data = response.json()
        title = data.get('title')
        summary = data.get('extract')
        page_url = data.get('content_urls', {}).get('desktop', {}).get('page')
        
        # Display the article details
        print(f"\nTitle: {title}\n")
        print(f"Summary: {summary}\n")
        return page_url
    else:
        print("Failed to fetch an article. Please try again.")
        return None

def main():
    print("=== Random Wikipedia Article Fetcher ===")
    while True:
        choice = input("\nChoose an option:\n1. Fetch a random article\n2. Exit\n> ")
        if choice == "1":
            page_url = fetch_random_article()
            if page_url:
                open_choice = input("\nDo you want to open the full article in your browser? (y/n): ").strip().lower()
                if open_choice == 'y':
                    webbrowser.open(page_url)
        elif choice == "2":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
