import requests

# Function to get video URL from API
def get_video_url(video_id):
    api_url = f"https://api.hotscope.tv/videos/video/{video_id}"
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
        video_url = data.get("video")
        return video_url
    else:
        raise Exception(f"Failed to fetch video URL for ID {video_id}. Status Code: {response.status_code}")

# Read values from values.txt
with open('values.txt', 'r') as file:
    id_values = file.read().splitlines()

# Iterate through each ID, fetch video URL, and save to url.txt
with open('url.txt', 'w') as url_file:
    for value in id_values:
        try:
            video_url = get_video_url(value)
            url_file.write(video_url + '\n')
            print(f"Video URL for ID {value} saved to url.txt")
        except Exception as e:
            print(f"Failed to fetch video URL for ID {value}. Error: {e}")
