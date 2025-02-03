import re
import requests
import json
import os

class LinkedinAutomate:
    def __init__(self, access_token, topic, description, image=None, yt_url=None):
        """
        :param access_token: LinkedIn access token
        :param topic: The 'title' or 'topic' of your post (string)
        :param description: The text content/description of your post (string)
        :param image: (Optional) A direct image URL if you want to share an image (string)
        :param yt_url: (Optional) YouTube video link if you want to share a YouTube video (string)
        """
        self.access_token = access_token
        self.topic = topic
        self.description = description
        self.image = image
        self.yt_url = yt_url
        
        # You can define any group IDs here
        self.python_group_list = [9247360]
        
        self.headers = {
            'Authorization': f'Bearer {self.access_token}',
            'Content-Type': 'application/json'
        }
        
        # We fetch the user ID once in main_func (or you could fetch it here).
        self.user_id = None

    def get_user_id(self):
        """
        Example user info endpoint to fetch your user (member) id from LinkedIn
        """
        url = "https://api.linkedin.com/v2/userinfo"
        response = requests.request("GET", url, headers=self.headers)
        response.raise_for_status()
        jsonData = response.json()
        return jsonData["sub"]
    
    def extract_video_id_from_youtube_url(self):
        """
        Extracts the video id from the given YouTube URL using a regex
        """
        pattern = r"^.*((youtu.be\/)|(v\/)|(\/u\/\w\/)|(embed\/)|(watch\?))\??v?=?([^#&?]*).*"
        match = re.findall(pattern, self.yt_url)
        if match:
            return match[0][-1]
        return None
    
    def get_youtube_thumbnail_url(self, video_id):
        """
        Constructs the thumbnail URL for the given video_id
        """
        return f"https://i.ytimg.com/vi/{video_id}/maxresdefault.jpg"
    
    def build_payload(self, feed_type="feed", group_id=None):
        """
        Builds the JSON payload for LinkedIn's ugcPosts API
        depending on whether you have a yt_url or an image or neither.
        """
        # Base structure common to all posts
        payload_dict = {
            "author": f"urn:li:person:{self.user_id}",
            "lifecycleState": "PUBLISHED",
            "specificContent": {
                "com.linkedin.ugc.ShareContent": {
                    "shareCommentary": {
                        "text": self.description
                    },
                    # We'll fill in shareMediaCategory and media below
                }
            },
            # If feed_type is group, we use "CONTAINER" visibility. Otherwise "PUBLIC".
            "visibility": {
                "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
                if feed_type == "feed" 
                else "CONTAINER"
            }
        }
        
        if feed_type == "group":
            payload_dict["containerEntity"] = f"urn:li:group:{group_id}"

        # Decide how to build the "media" part based on input
        media_category = None
        media_content = []

        # 1) If a YouTube URL was provided
        if self.yt_url:
            video_id = self.extract_video_id_from_youtube_url()
            if video_id:
                thumbnail_url = self.get_youtube_thumbnail_url(video_id)
                media_category = "ARTICLE"
                media_content = [
                    {
                        "status": "READY",
                        "description": {
                            "text": self.description
                        },
                        "originalUrl": self.yt_url,
                        "title": {
                            "text": self.topic
                        },
                        "thumbnails": [
                            {
                                "url": thumbnail_url
                            }
                        ]
                    }
                ]
        
        # 2) If an image was provided (and no yt_url)
        elif self.image:
            media_category = "ARTICLE"
            media_content = [
                {
                    "status": "READY",
                    "description": {
                        "text": self.description
                    },
                    "originalUrl": self.image,
                    "title": {
                        "text": self.topic
                    }
                }
            ]
        
        # 3) If no media at all, we can make it a text-only post.
        #    We do that by specifying "NONE" as shareMediaCategory 
        #    and no media array (or an empty array).
        if media_category is None:
            media_category = "NONE"

        payload_dict["specificContent"]["com.linkedin.ugc.ShareContent"]["shareMediaCategory"] = media_category
        
        # Only add "media" key if we have actual media to share
        if media_content:
            payload_dict["specificContent"]["com.linkedin.ugc.ShareContent"]["media"] = media_content
        
        return json.dumps(payload_dict)
    
    def post_to_feed(self):
        """
        Makes the POST request to LinkedIn UGC API for the regular feed
        """
        url = "https://api.linkedin.com/v2/ugcPosts"
        payload = self.build_payload(feed_type="feed")
        response = requests.post(url, headers=self.headers, data=payload)
        return response

    def post_to_group(self, group_id):
        """
        Makes the POST request to LinkedIn UGC API for a specific group
        """
        url = "https://api.linkedin.com/v2/ugcPosts"
        payload = self.build_payload(feed_type="group", group_id=group_id)
        response = requests.post(url, headers=self.headers, data=payload)
        return response

    def main_func(self):
        """
        The main entry point for our class.
        1) Fetch user ID
        2) Post to own feed
        3) Post to groups listed in self.python_group_list
        """
        self.user_id = self.get_user_id()
        print("User ID:", self.user_id)

        # Post to personal feed
        feed_response = self.post_to_feed()
        print("Feed post status:", feed_response.status_code, feed_response.text)
        
        # Post to groups
        for group_id in self.python_group_list:
            group_response = self.post_to_group(group_id)
            print(f"Group {group_id} post status:", group_response.status_code, group_response.text)

