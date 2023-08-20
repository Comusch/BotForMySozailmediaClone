import requests
import json
import os
class Bot:

    def __init__(self, bot_id, bot_password, url_base):
        self.bot_id = bot_id
        self.bot_password = bot_password
        self.url_base = url_base

    def login(self):
        url = self.url_base + 'login_bot/' + str(self.bot_id)
        data = {
            'password': self.bot_password
        }
        response = requests.post(url, data=data)
        print('Response:', response.status_code, response.text)
        return response.text

    def logout(self):
        url = self.url_base + 'logout_bot/' + str(self.bot_id)
        response = requests.post(url)
        print('Response:', response.status_code, response.text)
        return response.text

    def create_post(self, post_text, hashtags, image=None):
        url = self.url_base + 'Create_Post_bot/' + str(self.bot_id)
        data = {
            'password': self.bot_password,  # TODO: remove this field
            'post_text': post_text,
            'hashtags': hashtags
        }
        if image:
            data['image'] = image
        response = requests.post(url, data=data)
        print('Response:', response.status_code, response.text)

        try:
            response_data = response.json()  # Parse the JSON response
            post_id = response_data.get('post_id', -1)  # Use get() with default value
        except json.JSONDecodeError:
            print("Error decoding JSON response")
            post_id = -1  # Set post_id to a default value in case of an error

        return post_id

    def like_post(self, post_id):
        url = self.url_base + 'like_post_bot/' + str(self.bot_id)
        data = {
            'password': self.bot_password,  # TODO: remove this field
            'post_id': post_id
        }
        response = requests.post(url, data=data)
        print('Response:', response.status_code, response.text)
        return response.text

    def change_Description(self, description):
        url = self.url_base + 'change_Description_bot/' + str(self.bot_id)
        data = {
            'password': self.bot_password,  # TODO: remove this field
            'description': description
        }
        response = requests.post(url, data=data)
        print('Response:', response.status_code, response.text)
        return response.text

    def get_posts(self):
        url = self.url_base + 'get_bot_posts/' + str(self.bot_id)
        data = {
            'password': self.bot_password  # TODO: remove this field
        }
        response = requests.post(url, data=data)
        print('Response:', response.status_code, response.text)
        post_list = response.json()
        return post_list

    def get_post(self, post_id):
        url = self.url_base + 'get_bot_post/' + str(self.bot_id)
        data = {
            'password': self.bot_password,  # TODO: remove this field
            'post_id': post_id
        }
        response = requests.post(url, data=data)
        print('Response:', response.status_code, response.text)
        post = response.json()
        return post

    def get_comments(self, post_id):
        url = self.url_base + 'get_bot_comments/' + str(self.bot_id)
        data = {
            'password': self.bot_password,  # TODO: remove this field
            'post_id': post_id
        }
        response = requests.post(url, data=data)
        print('Response:', response.status_code, response.text)
        comment_list = response.json()
        return comment_list

    def create_comment(self, post_id, comment_text):
        url = self.url_base + 'create_comment_bot/' + str(self.bot_id)
        data = {
            'password': self.bot_password,  # TODO: remove this field
            'post_id': post_id,
            'comment_text': comment_text
        }
        response = requests.post(url, data=data)
        print('Response:', response.status_code, response.text)
        return response.text




