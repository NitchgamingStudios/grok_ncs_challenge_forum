from exceptions import PermissionDenied

class Post:
    def __init__(self, content, author):
        self.content = content
        self.author = author
        self.upvotes = set()

    def get_author(self):
        return self.author

    def get_content(self):
        return self.content

    def get_upvotes(self):
        return len(self.upvotes)

    def set_content(self, content, by_user):
        if by_user == self.author:
            self.content = content
        else:
            raise PermissionDenied("You do not have permission to edit this post.")

    def upvote(self, by_user):
        if by_user not in self.upvotes:
            self.upvotes.add(by_user)
        else:
            raise PermissionDenied("You can only upvote once.")