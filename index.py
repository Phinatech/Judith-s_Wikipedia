import requests
import webbrowser

def fetch_random_article():
    # Wikipedia API URL for fetching random articles
    url = "https://en.wikipedia.org/api/rest_v1/page/random/summary"
    response = requests.get(url)
    
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



