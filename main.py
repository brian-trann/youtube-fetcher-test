from googleapiclient.discovery import build
from youtube_transcript_api import YouTubeTranscriptApi
from datetime import datetime, timedelta

class YouTubeAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.youtube = build('youtube', 'v3', developerKey=self.api_key)
    
    def get_channel_id(self, username):
        request = self.youtube.channels().list(
            part='id',
            forHandle=username
        )
        response = request.execute()
        
        if 'items' in response and len(response['items']) > 0:
            return response['items'][0]['id']
        else:
            raise ValueError("No channel found for the provided username.")
    
    def get_latest_videos(self, channel_id, hours):
        now = datetime.utcnow()
        time_delta = now - timedelta(hours=hours)
        published_after = yesterday.isoformat("T") + "Z"

        request = self.youtube.search().list(
            part='snippet',
            channelId=channel_id,
            publishedAfter=published_after,
            maxResults=50,
            order='date'
        )
        response = request.execute()
        
        video_ids = [item['id']['videoId'] for item in response['items'] if item['id']['kind'] == 'youtube#video']
        return video_ids
    
    def get_video_details(self, video_id):
        request = self.youtube.videos().list(
            part='snippet',
            id=video_id
        )
        response = request.execute()
        
        if 'items' in response and len(response['items']) > 0:
            return response['items'][0]['snippet']
        else:
            raise ValueError("No video found for the provided video ID.")

    def get_video_transcript(self, video_id):
        try:
            transcript = YouTubeTranscriptApi.get_transcript(video_id)
            return transcript
        except Exception as e:
            raise ValueError(f"Could not fetch transcript: {e}")
        
    def get_video_transcript_as_string(self, video_id):
        try:
            transcript = YouTubeTranscriptApi.get_transcript(video_id)
            transcript_text = " ".join([entry['text'] for entry in transcript])
            return transcript_text
        except Exception as e:
            raise ValueError(f"Could not fetch transcript: {e}")

if __name__ == '__main__':
    
    API_KEY = ""
    youtube_api = YouTubeAPI(API_KEY)
    
    username = "Fireship"
    try:
        channel_id = youtube_api.get_channel_id(username)
        
        latest_videos = youtube_api.get_latest_videos(channel_id, 24)
        
        for video_id in latest_videos:
            video_details = youtube_api.get_video_details(video_id)
            print(f"Title: {video_details['title']}")
            transcript = youtube_api.get_video_transcript_as_string(video_id)
            print(transcript)

    except Exception as e:
        print(f"An error occurred: {e}")
