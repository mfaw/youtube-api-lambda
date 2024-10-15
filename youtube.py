import json
import requests
import os

# Replace with your YouTube Data API key
API_KEY = os.getenv('YOUTUBE_API_KEY','')


def lambda_handler(event, context):
    # Get channel username from the request parameters (or hardcode for testing)
    channel_name = event.get('queryStringParameters', {}).get('username', 'stakpak')
    # YouTube Data API URL to get channel info by username
    # YouTube Data API URL to search for channels by name
    search_url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&type=channel&q={channel_name}&key={API_KEY}"

    try:
        # Make a request to the YouTube API to search for the channel
        search_response = requests.get(search_url)
        search_data = search_response.json()

        # Check if the search returned any results
        if 'items' not in search_data or len(search_data['items']) == 0:
            return {
                'statusCode': 404,
                'body': json.dumps({'error': 'Channel not found.'})
            }

        # Get the channel ID from the search results
        channel_id = search_data['items'][0]['id']['channelId']

        # YouTube Data API URL to get channel info by channel ID
        channel_url = f"https://www.googleapis.com/youtube/v3/channels?part=snippet,statistics&id={channel_id}&key={API_KEY}"

        # Make a request to get channel info
        response = requests.get(channel_url)
        data = response.json()

        # Check if the channel data was found
        if 'items' not in data or len(data['items']) == 0:
            return {
                'statusCode': 404,
                'body': json.dumps({'error': 'Channel not found.'})
            }

        # Extract the relevant data
        channel_data = data['items'][0]
        snippet = channel_data['snippet']
        statistics = channel_data['statistics']

        result = {
            'channel_name': snippet['title'],
            'description': snippet['description'],
            'subscribers': statistics.get('subscriberCount', 'N/A'),
            'total_views': statistics.get('viewCount', 'N/A'),
            'video_count': statistics.get('videoCount', 'N/A')
        }

        # Return the result as a JSON response
        return {
            'statusCode': 200,
            'body': json.dumps(result)
        }

    except Exception as e:
        # Handle exceptions gracefully
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
