from googleapiclient.discovery import build
import pandas as pd
import yaml

with open("secrets.yml", "r") as file:
    secrets = yaml.safe_load(file)

api_keys = [secrets['api_key'], secrets['api_key1'], secrets['api_key2'], secrets['api_key3']]
current_key_index = 0

def get_youtube_service():
    global current_key_index
    while current_key_index < len(api_keys):
        try:
            youtube = build('youtube', 'v3', developerKey=api_keys[current_key_index])
            # Basit bir istek yaparak API anahtarını test edin
            youtube.search().list(q="test", part="id", maxResults=1).execute()
            return youtube
        except Exception:
            print(f"API key {api_keys[current_key_index]} failed: API limit aşımı yapıldı")
            current_key_index += 1
    raise Exception("All API keys have reached their limit.")

def get_video_id(query):
    youtube = get_youtube_service()
    search_response = youtube.search().list(
        q=query,
        part="id",
        type="video",
        maxResults=1
    ).execute()

    if 'items' in search_response and len(search_response['items']) > 0:
        item = search_response['items'][0]['id']
        if item['kind'] == 'youtube#video':
            return item['videoId']
        elif item['kind'] == 'youtube#playlist':
            print("This result is a playlist, not a video.")
            return None
    else:
        print("No video found for this query.")
        return None

def pull_comments(video_id, max_comments=100):
    comments = []
    youtube = get_youtube_service()
    request = youtube.commentThreads().list(
        part="snippet",
        videoId=video_id,
        maxResults=100
    )
    response = request.execute()

    while response and len(comments) < max_comments:
        for item in response['items']:
            if len(comments) >= max_comments:
                break
            comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
            like_count = item['snippet']['topLevelComment']['snippet']['likeCount']
            published_at = item['snippet']['topLevelComment']['snippet']['publishedAt']
            author = item['snippet']['topLevelComment']['snippet']['authorDisplayName']

            comments.append([author, comment, like_count, published_at])

        if 'nextPageToken' in response and len(comments) < max_comments:
            request = youtube.commentThreads().list(
                part="snippet",
                videoId=video_id,
                pageToken=response['nextPageToken'],
                maxResults=100
            )
            response = request.execute()
        else:
            break

    return pd.DataFrame(comments, columns=['Author', 'Comment', 'Like_Count', 'Published_At'])

"""# Test
video_id = get_video_id("polinomlar")
comments = pull_comments(video_id)
print(comments)
print("Comments successfully retrieved.")
comments.to_csv('youtube_comments_1.csv', index=False)
print("Comments successfully saved.")"""