import requests

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
        return response.text

    def like_post(self, post_id):
        url = self.url_base + 'like_post_bot/' + str(self.bot_id)
        data = {
            'password': self.bot_password,  # TODO: remove this field
            'post_id': post_id
        }
        response = requests.post(url, data=data)
        print('Response:', response.status_code, response.text)
        return response.text

    def change_Description(self):
        url = self.url_base + 'change_Description_bot/' + str(self.bot_id)
        data = {
            'password': self.bot_password,  # TODO: remove this field
            'description': 'This is a bot'
        }
        response = requests.post(url, data=data)
        print('Response:', response.status_code, response.text)
        return response.text

