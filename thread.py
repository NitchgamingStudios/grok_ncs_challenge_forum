from exceptions import PermissionDenied

class Thread:
    def __init__(self, title, first_post):
        self.title = title
        self.owner = first_post.get_author()
        self.tags = []
        self.posts = [first_post]

    def get_owner(self):
        return self.owner

    def get_title(self):
        return self.title

    def get_tags(self):
        return sorted(self.tags)

    def get_posts(self):
        return self.posts

    def publish_post(self, post):
        self.posts.append(post)

    def remove_post(self, post, by_user):
        if post in self.posts:
            if by_user == post.get_author():
                self.posts.remove(post)
            else:
                raise PermissionDenied("You do not have permission to remove this post.")

    def set_title(self, title, by_user):
        if by_user == self.owner:
            self.title = title
        else:
            raise PermissionDenied("You do not have permission to edit this thread's title.")

    def set_tags(self, tag_list, by_user):
        if by_user == self.owner:
            self.tags = tag_list
        else:
            raise PermissionDenied("You do not have permission to edit this thread's tags.")