from datetime import datetime
import requests


def fetch_data():
    url = "https://jsonplaceholder.typicode.com/posts/1"

    response = requests.get(url)

    if response.status_code == 200:
        return response.json()

    return {}


def generate_log(post):
    log_data = [
        "User logged in",
        "User updated profile",
        "Report exported"
    ]

    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    with open(filename, "w") as file:
        for entry in log_data:
            file.write(f"{entry}\n")

        file.write("\nAPI DATA\n")
        file.write(f"Title: {post.get('title', 'No title found')}\n")
        file.write(f"Body: {post.get('body', 'No body found')}\n")

    return filename


def main():
    post = fetch_data()

    print("Fetched Post Title:", post.get("title", "No title found"))

    filename = generate_log(post)

    print(f"Log written to {filename}")


if __name__ == "__main__":
    main()