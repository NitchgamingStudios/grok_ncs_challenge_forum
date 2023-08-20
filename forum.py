from post import Post
from thread import Thread

class Forum:
    def __init__(self):
        self.threads = []

    def get_threads(self):
        return self.threads

    def publish(self, title, content, author):
        first_post = Post(content, author)
        thread = Thread(title, first_post)
        self.threads.append(thread)
        return thread

    def search_by_tag(self, tag):
        matching_threads = []
        for thread in self.threads:
            if tag in thread.get_tags():
                matching_threads.append(thread)
        return matching_threads

    def search_by_author(self, author):
        matching_posts = []
        for thread in self.threads:
            for post in thread.get_posts():
                if post.get_author() == author:
                    matching_posts.append(post)
        return matching_posts