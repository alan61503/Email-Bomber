import time
import requests

def open_links_from_file(file_path, delay=2):
    """
    Reads a list of URLs from a file and opens each one with a delay.
    :param file_path: Path to the file containing URLs (one per line)
    :param delay: Delay in seconds between requests
    """
    with open(file_path, 'r') as f:
        links = [line.strip() for line in f if line.strip()]
    for idx, link in enumerate(links, 1):
        try:
            print(f"Opening link {idx}: {link}")
            response = requests.get(link)
            print(f"Status code: {response.status_code}")
        except Exception as e:
            print(f"Error opening {link}: {e}")
        time.sleep(delay)

if __name__ == "__main__":
    file_path = input("Enter the path to the file containing links: ")
    open_links_from_file(file_path)
