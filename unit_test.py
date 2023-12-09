import unittest
from Post import POST, Blog, User
from post_dict import post_dict





class TestBlogClass(unittest.TestCase):

    def test_create_post(self):
        blog = Blog('test blog')
        user_id = 485
        username = 'Hessam'
        user = User(user_id, username)
        # user.SaveUser(user_id, username)
        print("Initial post_dict:", post_dict)
        print()
        print('-------------------------------------------------------------------------')
        print()
        blog.create_post(
            title="Test Post",
            content="This is a test post.",
            author=user,  # Replace with your actual instance of User
            created_at="2023-01-01",
            updated_at="2023-01-02"
        )

        # Print post_dict after creating the post
        print("post_dict after create_post:", post_dict)


    def test_remove_post(self):
        blog = Blog('test blog')
        user_id = 485
        username = 'Sahar'
        user = User(user_id, username)
        print("Initial post_dict:", post_dict)
        print()
        print('-------------------------------------------------------------------------')
        print()
        blog.create_post( title="Test Remove",
            content="This is a test post for remove functionality.",
            author=user,  # Replace with your actual instance of User
            created_at="2023-01-01",
            updated_at="2023-01-02")
        
        blog.remove_post("Test Remove")
        print("Initial post_dict:", post_dict)

if __name__ == '__main__':
    unittest.main()
