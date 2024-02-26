# Implement a script to fetch new episodes from target podcasts using their RSS feeds.
import os
import requests
import feedparser


def download_file(url, filename):
    """Download a file from a given URL."""
    response = requests.get(url)
    with open(filename, "wb") as file:
        file.write(response.content)
    print(f"Downloaded {filename}")


def main():
    # Ask the user for the podcast RSS feed URL
    rss_url = input("Enter the RSS feed URL of the podcast: ")

    # Parse the RSS feed
    feed = feedparser.parse(rss_url)

    # Directory to save episodes
    save_dir = "podcast_episodes"
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    # Assuming the latest episode is the first entry
    latest_episode = feed.entries[0]

    # Assuming the episode's audio file URL is in 'links'
    audio_url = latest_episode.links[0]["href"]
    filename = os.path.join(save_dir, latest_episode.title + ".mp3")

    # Download the latest episode
    download_file(audio_url, filename)


if __name__ == "__main__":
    main()
