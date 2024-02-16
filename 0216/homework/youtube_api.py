from googleapiclient.discovery import build
from googleapiclient.errors import HttpError



# 유튜브 API 클라이언트 빌드
youtube = build('youtube', 'v3', developerKey='AIzaSyAgV1ieURSdPWGizkI6QMHYnRca46lna1o')

def get_playlist_items(playlist_id):
    try:
        # playlistItems() 메소드를 사용하여 플레이리스트 아이템 가져오기
        response = youtube.playlistItems().list(
            part='snippet',
            maxResults=50,  # 최대 50개의 아이템 가져오기
            playlistId=playlist_id
        ).execute()

        # 가져온 플레이리스트 아이템 출력
        for item in response['items']:
            video_title = item['snippet']['title']
            video_id = item['snippet']['resourceId']['videoId']
            video_url = f'https://www.youtube.com/watch?v={video_id}'
            print(f'Title: {video_title}, Video URL: {video_url}')

    except HttpError as e:
        print(f'An HTTP error occurred: {e}')

# 사용 예시
playlist_id = 'PLKQLnbmCz_8K4ofuuWvKkbiprI7LamhMh'  # 자신의 플레이리스트 ID로 대체해주세요
get_playlist_items(playlist_id)