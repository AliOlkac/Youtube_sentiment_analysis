from googleapiclient.discovery import build
import pandas as pd

# YouTube API ayarları
api_key = 'Mal KAAN'
video_id = 'Mal Meret'  # Yorumlarını çekmek istediğiniz videonun ID'si

youtube = build('youtube', 'v3', developerKey=api_key)

# Yorumları çekme fonksiyonu
def get_comments(video_id):
    comments = []
    request = youtube.commentThreads().list(
        part="snippet",
        videoId=video_id,
        maxResults=100
    )
    response = request.execute()

    while response:
        for item in response['items']:
            comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
            like_count = item['snippet']['topLevelComment']['snippet']['likeCount']
            published_at = item['snippet']['topLevelComment']['snippet']['publishedAt']
            author = item['snippet']['topLevelComment']['snippet']['authorDisplayName']

            comments.append([author, comment, like_count, published_at])

        if 'nextPageToken' in response:
            request = youtube.commentThreads().list(
                part="snippet",
                videoId=video_id,
                pageToken=response['nextPageToken'],
                maxResults=100
            )
            response = request.execute()
        else:
            break

    return comments

# Yorumları çekip CSV'ye kaydetme
comments_data = get_comments(video_id)
comments_df = pd.DataFrame(comments_data, columns=['Author', 'Comment', 'LikeCount', 'PublishedAt'])
comments_df.to_csv('youtube_comments.csv', index=False)
print("Yorumlar başarıyla kaydedildi.")
