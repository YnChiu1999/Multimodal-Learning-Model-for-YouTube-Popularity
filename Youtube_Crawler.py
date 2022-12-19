import requests
import csv
from datetime import datetime
import os
from _get_top50_YouTube import getTop50ID  # user-defined

### Step 0：Get "YOUTUBE_API_KEY" and "Channel ID"
YOUTUBE_API_KEY = "YOUTUBE_API_KEY"
# Get the Channel ID for YouTube Crawler
# Get the Channel ID: https://commentpicker.com/youtube-channel-id.php
list_youtube_channel_id = ["UC0Q-fBheHysYWz9ObSEzMdA", "UCq5lbTl1VD0PLtHteglqZfA", 'UC3O6-k2zKhLOt4rGU3fOeyg']
# Get the Channel ID by "_get_top50_YouTube.getTop50ID"
# list_youtube_channel_id = topForTW(YOUTUBE_API_KEY)

# Make the folder for saving downloaded image
os.mkdir(f"./download_image/")

### Step 1：YouTube Crawler
def main():
    all_video_info = []
    for youtube_channel_id in list_youtube_channel_id:
        # 1) Get "Channel ID"
        youtube_crawler = YouTubeCrawler(YOUTUBE_API_KEY)
        channel_subCount = youtube_crawler.getsub_count(youtube_channel_id)
        print(channel_subCount)
        # 2)  Get "Channel uploads ID"
        uploads_id = youtube_crawler.get_channel_uploads_id(youtube_channel_id)
        print(uploads_id)
        # 3) Get "Video ID"
        all_video_ids = []
        next_page_token = ''
        while 1:
            video_ids, next_page_token = youtube_crawler.get_playlist(uploads_id, page_token=next_page_token, max_results=100)
            all_video_ids.extend(video_ids)
            if not next_page_token:
                break
            # if not len(all_video_ids)>5:
            #     break
        print(len(all_video_ids))
        print(all_video_ids)

        ## 2.Get "video_info" from "Channel uploads ID"
        for video_id in all_video_ids:
            print("----------------------")
            video_info = youtube_crawler.get_video(video_id)
            video_info['subscriberCount'] = channel_subCount
            print(video_info)
            all_video_info.append(video_info)
            # # Comments reply (if need)
            # next_page_token = ''
            # while 1:
            #     comments, next_page_token = youtube_crawler.get_comments(video_id, page_token=next_page_token)
            #     print(comments)
            #     if not next_page_token:
            #         break

    ## 3.寫入csv檔、
    labels = ['id', 'channelTitle', 'subscriberCount', 'publishedAt', 'title', 'likeCount', 'commentCount', 'viewCount', 'video_url']
    try:
        with open('YT_output.csv', 'a+', encoding = 'utf-8-sig', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=labels)
            writer.writeheader()
            for elem in all_video_info:
                writer.writerow(elem)
    except IOError:
        print("I/O error")

### Subroutine：YouTube Crawler
class YouTubeCrawler():
    ## 1. Each request needs to be accompanied by API Key
    def __init__(self, api_key):
        self.base_url = "https://www.googleapis.com/youtube/v3/"
        self.api_key = api_key

    ## 2. Return data to be converted to JSON
    def get_html_to_json(self, path):
        """組合 URL 後 GET 網頁並轉換成 JSON"""
        api_url = f"{self.base_url}{path}&key={self.api_key}"
        r = requests.get(api_url)
        if r.status_code == requests.codes.ok:
            data = r.json()
        else:
            data = None
        return data

    ## 3. Return "Subscriber Count"
    def getsub_count(self, channel_id, part='snippet,statistics'):
        """取得頻道上傳影片清單的ID"""
        path = f'channels?part={part}&id={channel_id}'
        data = self.get_html_to_json(path)
        try:
            subCount = data['items'][0]["statistics"]["subscriberCount"]
        except KeyError:
            subCount = None
        return subCount

    ## 4. Return "Channel uploads ID"
    def get_channel_uploads_id(self, channel_id, part='contentDetails'):
        """取得頻道上傳影片清單的ID"""
        path = f'channels?part={part}&id={channel_id}'
        data = self.get_html_to_json(path)
        try:
            uploads_id = data['items'][0]['contentDetails']['relatedPlaylists']['uploads']
        except KeyError:
            uploads_id = None
        return uploads_id

    ## 5. Return "Video ID"。
    def get_playlist(self, playlist_id, part='contentDetails', page_token='', max_results=100):
        """取得影片清單ID中的影片"""
        path = f'playlistItems?part={part}&playlistId={playlist_id}&maxResults={max_results}&pageToken={page_token}'
        data = self.get_html_to_json(path)
        if not data:
            return []
        # 下一頁的數值
        next_page_token = data.get('nextPageToken', '')
        video_ids = []
        for data_item in data['items']:
            video_ids.append(data_item['contentDetails']['videoId'])
        return video_ids, next_page_token

    ## 6. Return "Video info"
    def get_video(self, video_id, part='snippet,statistics'):
        """取得影片資訊"""
        path = f'videos?part={part}&id={video_id}'
        data = self.get_html_to_json(path)
        if not data:
            return {}

        # The following is a compilation and extraction of the required information
        data_item = data['items'][0]

        try:
            # 2019-09-29T04:17:05Z
            time_ = datetime.strptime(data_item['snippet']['publishedAt'], '%Y-%m-%dT%H:%M:%SZ')
        except ValueError:
            # Date format error
            time_ = None

        url_ = f"https://www.youtube.com/watch?v={data_item['id']}"

        try:
            comment_ = data_item['statistics']['commentCount']
        except:
            # Message deactivation
            comment_ = 0

        try:
            like_ = data_item['statistics']['likeCount']
        except:
            # Comment Likes
            like_ = 0
        info = {
            'id': data_item['id'],                                          # Video ID
            'channelTitle': data_item['snippet']['channelTitle'],           # Channel Title
            'publishedAt': time_,                                           # published Time
            'video_url': url_,                                              # Video url
            'title': data_item['snippet']['title'],                         # Video Title
            # 'description': data_item['snippet']['description'],           # Video Description
            'likeCount': like_,                                             # Likes Count
            # 'dislikeCount': data_item['statistics']['dislikeCount'],      # Unlikes Count
            'commentCount': comment_,                                       # Comments Count
            'viewCount': data_item['statistics']['viewCount']               # View Count
        }
        f = open(f"./download_image/{data_item['id']}.jpg", 'wb')           # Thumbnails
        response = requests.get(f"https://i.ytimg.com/vi/{data_item['id']}/0.jpg")
        f.write(response.content)
        f.close()
        return info

    ## 7. Return "Video comments info"
    def get_comments(self, video_id, page_token='', part='snippet', max_results=100):
        """取得影片留言"""
        path = f'commentThreads?part={part}&videoId={video_id}&maxResults={max_results}&pageToken={page_token}'
        data = self.get_html_to_json(path)
        if not data:
            return [], ''
        # 下一頁的數值
        next_page_token = data.get('nextPageToken', '')

        # 以下整理並提取需要的資料
        comments = []
        for data_item in data['items']:
            data_item = data_item['snippet']
            top_comment = data_item['topLevelComment']
            try:
                # 2020-08-03T16:00:56Z
                time_ = datetime.strptime(top_comment['snippet']['publishedAt'], '%Y-%m-%dT%H:%M:%SZ')
            except ValueError:
                # 日期格式錯誤
                time_ = None

            if 'authorChannelId' in top_comment['snippet']:
                ru_id = top_comment['snippet']['authorChannelId']['value']
            else:
                ru_id = ''

            ru_name = top_comment['snippet'].get('authorDisplayName', '')
            if not ru_name:
                ru_name = ''

            comments.append({
                'reply_id': top_comment['id'],                                 # Comment ID
                'ru_id': ru_id,                                                # Comment user ID
                'ru_name': ru_name,                                            # Comment username
                'reply_time': time_,                                           # Comment published Time
                'reply_content': top_comment['snippet']['textOriginal'],       # Comment content
                'rm_positive': int(top_comment['snippet']['likeCount']),       # Comment likes count
                'rn_comment': int(data_item['totalReplyCount'])                # Comment reply count
            })
        return comments, next_page_token

if __name__ == "__main__":
    main()