from googleapiclient.discovery import build
import pandas as pd

api_key = 'AIzaSyDk7L-mTjNCW1xB9QJF6zVi1jdFOh3hCac'
youtube = build("youtube", "v3", developerKey=api_key)


def get_video_id(query):
    search_response = youtube.search().list(
        q=query,
        part="id",
        type="video",
        maxResults=1
    ).execute()

    # items listesi içinde veri olup olmadığını kontrol edin
    if 'items' in search_response and len(search_response['items']) > 0:
        item = search_response['items'][0]['id']

        # Video mu yoksa oynatma listesi mi olduğunu kontrol edin
        if item['kind'] == 'youtube#video':
            video_id = item['videoId']
            return video_id

        elif item['kind'] == 'youtube#playlist':
            print("Bu sonuç bir oynatma listesi, video değil.")
            return None
    else:
        print("Bu arama sorgusuna uygun bir video bulunamadı.")
        return None
# Yorumları çekme fonksiyonu

def pull_comments(video_id, max_comments=100):
    youtube = build('youtube', 'v3', developerKey=api_key)
    comments = []
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
print("Yorumları başarıyla çekti.")
# Yorumları kaydet
comments.to_csv('youtube_comments_1.csv', index=False)
print("Yorumlar başarıyla kaydedildi.")"""
