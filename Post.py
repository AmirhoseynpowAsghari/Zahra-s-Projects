from user_dict import user_dict
import argparse
from post_dict  import post_dict
import json
import logging

#
import functools
import datetime

#For tokenizing words in lambda search section / I changed my mind and I have used another method 
# I want to tokenize the text and and search in words

import nltk
from nltk.tokenize import word_tokenize

logging.basicConfig(filename='log.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def log_user_activity(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        
        # Logging
        action_name = func.__name__.replace('_', ' ').capitalize()
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_message = f"{timestamp} - {action_name} - {result}"
        
        logging.info(log_message)
        
        return result
    
    return wrapper

class POST:
    def __init__(self, title, content, author, created_at, updated_at):
        self.title = title
        self.content = content
        self.author = author  # This should be an instance of the User class
        self.created_at = created_at
        self.updated_at = updated_at

    def get_author_id(self):
        # Assuming User class has a method to get user ID
        return self.author.get_user_id()   
    

class User:
    
    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username

    def get_user_id(self):
        return self.user_id
    
    @log_user_activity
    def SaveUser(self, user_id, username):
        new_user = User(user_id, username)
        if new_user.user_id not in user_dict:
            user_dict[user_id] = [username]
        
        else:
            user_dict[user_id].append(username)
        
        logging.info(f"A new user has been created with this username {username}")

        with open("user_dict.py", 'w') as dict_file:
            dict_file.write('user_dict = ')
            json.dump(user_dict, dict_file, indent=4)



class Blog:

    def __init__(self, name):
        self.name = name
        self.posts = []  # Initialize posts as an instance attribute

    @log_user_activity
    def create_post(self, title, content, author, created_at, updated_at):
        new_post = POST(title, content, author, created_at, updated_at)
        if new_post.title not in post_dict:
            post_dict[title] = [{'content': content, 'author': author.get_user_id()}]
        else:
            post_dict[title].append({'content': content, 'author': author.get_user_id()})
        
        logging.info(f"A new post has been created with this title {new_post.title}")

        with open("post_dict.py", "w") as dict_file:
            dict_file.write('post_dict = ')
            json.dump(post_dict, dict_file, indent=4)
        # Append to the post_list from post_list.py
        return new_post
    @log_user_activity
    def remove_post(self, title_to_remove):
        if title_to_remove in post_dict:
            del post_dict[title_to_remove]
            with open("post_dict.py", "w") as dict_file:
                dict_file.write('post_dict = ')
                json.dump(post_dict, dict_file, indent=4)
            print(f"Post '{title_to_remove}' removed successfully from post_dict")
        else:
            print(f"Post with title '{title_to_remove}' not found in post_dict")


    def search_posts(self, query):
        matching_posts = []

        for post_title, post_content_list in post_dict.items():
            for post_content in post_content_list:
                if isinstance(post_content, str):
                    # If post_content is a string
                    if query.lower() in post_title.lower() or query.lower() in post_content.lower():
                        matching_posts.append((post_title, post_content))
                elif isinstance(post_content, dict):
                    # If post_content is a dictionary
                    if query.lower() in post_title.lower() or query.lower() in post_content['content'].lower():
                        matching_posts.append((post_title, post_content))

        return matching_posts
    

    def lambda_search_posts(self, query):
        filtered_posts = filter(lambda item: query.lower() in (" ".join(item) if isinstance(item[1], str) else item[1]['content']).lower(),
                                [(post_title, post_content) for post_title, post_content_list in post_dict.items() for post_content in post_content_list])
        return list(filtered_posts)
    
    
    def filtering_posts_by_author(self, author):
        posts_by_author = [post for post in self.posts if post.author.username == author]
        return posts_by_author

    def display_posts(self):
        for post in self.posts:
            yield post



    
def main():
    parser = argparse.ArgumentParser(description="Manage a simple blog using command-line interface")
    parser.add_argument("--create_user", action="store_true", help="Create a new user")
    parser.add_argument("--create_post", action="store_true", help="Create a new blog post")
    parser.add_argument("--remove_post", action="store_true", help="Remove a blog post")
    parser.add_argument("--search_posts", action="store_true", help="Search for posts containing a specific query")
    parser.add_argument("--filter_by_author", type=str, help="Filter posts by author")

    args = parser.parse_args()
    
    blog1 = Blog(name="My Blog")

    if args.create_user:
        user_id = input("Enter your Id: ")
        username = input("Enter your username: ")
        user = User(user_id, username)
        print(f"User '{user.username}' created successfully")
        user.SaveUser(user_id, username)

    elif args.create_post:
        title = input("Enter post title: ")
        content = input("Enter post content: ")
        created_at = input("Enter post creation date: ")
        updated_at = input("Enter post update date: ")
        print(f'Which user are you who want to post \n {user_dict}')
        user_id = input("Enter your Id: ")
        username = input("Enter your username: ")
        user = User(user_id, username)
        post = blog1.create_post(title, content, user, created_at, updated_at)
        print(f"Post '{post.title}' created successfully")

    elif args.remove_post:
        title_to_remove = input("Enter the title of the post to remove: ")
        blog1.remove_post(title_to_remove)

    elif args.search_posts:
        search_query = str(input('Give search value:'))
        matching_posts = blog1.search_posts(search_query)
        print(f"\nPosts matching '{search_query}':")
        for post in matching_posts:
            print(f"{post}")

    elif args.filter_by_author:
        author_query = args.filter_by_author
        filtered_posts = blog1.filtering_posts_by_author(author_query)
        print(f"\nPosts by {author_query}:")
        for post in filtered_posts:
            print(f"Post: {post.title} by {post.author.username}")

    else:
        print("No valid action specified. Use --help for available options.")


if __name__ == "__main__":
    main()

