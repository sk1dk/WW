import requests
from tqdm import tqdm
import os

# Function to download video and show progress bar
def download_video(video_url, destination_path):
    response = requests.get(video_url, stream=True)
    total_size = int(response.headers.get('content-length', 0))
    block_size = 1024  # 1 Kibibyte

    # Use tqdm to show progress bar
    with tqdm(total=total_size, unit='B', unit_scale=True, unit_divisor=1024, desc=os.path.basename(destination_path)) as pbar:
        with open(destination_path, 'wb') as file:
            for data in response.iter_content(block_size):
                pbar.update(len(data))
                file.write(data)

# Read URLs from url.txt
with open('url.txt', 'r') as file:
    video_urls = file.read().splitlines()

# Create a directory to save the downloaded videos
if not os.path.exists('downloaded_videos'):
    os.makedirs('downloaded_videos')

# Iterate through each URL and download the corresponding video
for url in video_urls:
    video_id = url.split('/')[-1].split('.')[0]
    destination_path = f"downloaded_videos/{video_id}.mp4"

    try:
        download_video(url, destination_path)
        print(f"Video {video_id}.mp4 downloaded successfully.")
    except Exception as e:
        print(f"Failed to download video {video_id}.mp4. Error: {e}")
