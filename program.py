from forum import Forum
from post import Post
from exceptions import PermissionDenied

# Create a forum
forum = Forum()

def create_thread():
    title = input("Enter thread title: ")
    content = input("Enter the first post content: ")
    author = input("Enter your username: ")
    
    first_post = Post(content, author)
    thread = forum.publish(title, content, author)
    
    print(f"Thread '{title}' created successfully!")
    return thread

def add_post(thread):
    content = input("Enter post content: ")
    author = input("Enter your username: ")
    
    new_post = Post(content, author)
    thread.publish_post(new_post)
    
    print("Post added successfully!")

def edit_post(post):
    new_content = input("Enter new post content: ")
    by_user = input("Enter your username: ")
    
    try:
        post.set_content(new_content, by_user)
        print("Post edited successfully!")
    except PermissionDenied as e:
        print(e)

def upvote_post(post):
    user = input("Enter your username: ")
    
    try:
        post.upvote(user)
        print(f"Upvoted post by {post.get_author()} successfully!")
    except PermissionDenied as e:
        print(e)

def menu():
    while True:
        print("\nForum Menu:")
        print("1. Create a Thread")
        print("2. Add a Post to a Thread")
        print("3. Edit a Post")
        print("4. Upvote a Post")
        print("5. Exit")
        
        choice = input("Enter your choice (1/2/3/4/5): ")
        
        if choice == "1":
            create_thread()
        elif choice == "2":
            threads = forum.get_threads()
            if not threads:
                print("No threads available. Create a thread first.")
            else:
                print("\nThreads:")
                for i, thread in enumerate(threads, start=1):
                    print(f"{i}. {thread.get_title()}")

                thread_num = int(input("Enter the thread number to add a post to: ")) - 1
                if 0 <= thread_num < len(threads):
                    add_post(threads[thread_num])
                else:
                    print("Invalid thread number.")
        elif choice == "3":
            threads = forum.get_threads()
            if not threads:
                print("No threads available.")
            else:
                print("\nThreads:")
                for i, thread in enumerate(threads, start=1):
                    print(f"{i}. {thread.get_title()}")

                thread_num = int(input("Enter the thread number to edit a post in: ")) - 1
                if 0 <= thread_num < len(threads):
                    posts = threads[thread_num].get_posts()
                    if not posts:
                        print("No posts in this thread.")
                    else:
                        print("\nPosts in this Thread:")
                        for i, post in enumerate(posts, start=1):
                            print(f"{i}. {post.get_content()}")

                        post_num = int(input("Enter the post number to edit: ")) - 1
                        if 0 <= post_num < len(posts):
                            edit_post(posts[post_num])
                        else:
                            print("Invalid post number.")
                else:
                    print("Invalid thread number.")
        elif choice == "4":
            threads = forum.get_threads()
            if not threads:
                print("No threads available.")
            else:
                print("\nThreads:")
                for i, thread in enumerate(threads, start=1):
                    print(f"{i}. {thread.get_title()}")

                thread_num = int(input("Enter the thread number to upvote a post in: ")) - 1
                if 0 <= thread_num < len(threads):
                    posts = threads[thread_num].get_posts()
                    if not posts:
                        print("No posts in this thread.")
                    else:
                        print("\nPosts in this Thread:")
                        for i, post in enumerate(posts, start=1):
                            print(f"{i}. {post.get_content()}")

                        post_num = int(input("Enter the post number to upvote: ")) - 1
                        if 0 <= post_num < len(posts):
                            upvote_post(posts[post_num])
                        else:
                            print("Invalid post number.")
                else:
                    print("Invalid thread number.")
        elif choice == "5":
            print("Exiting the forum. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option (1/2/3/4/5).")

if __name__ == "__main__":
    menu()
