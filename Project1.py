"""
Build a CLI Blog Draft Manager -
A command-line interface for managing blog posts 
stored in files using OOP.
Your BlogPost should have four attributes:
: title, author, date_created and content.

"""

# BlogPost

import os
from datetime import datetime

class BlogPost:
    def __init__(self, title, author, content):
        self.title = title
        self.author = author
        self.date_created = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.content = content

class BlogManager:
    def __init__(self):
        self.drafts_dir = "drafts"
        if not os.path.exists(self.drafts_dir):
            os.makedirs(self.drafts_dir)

    def create(self):
        try:
            title = input("Title: ")
            if not title:
                print("Title cannot be empty.")
                return
            author = input("Author: ")
            if not author:
                print("Author cannot be empty.")
                return
            content = input("Content: ")
            if not content:
                print("Content cannot be empty.")
                return
            post = BlogPost(title, author, content)
            filename = f"{self.drafts_dir}/{title.replace(' ', '_')}.txt"
            if os.path.exists(filename):
                print("Draft with this title already exists.")
                return
            with open(filename, "w") as file:
                file.write(f"Title: {post.title}\nAuthor: {post.author}\nDate: {post.date_created}\nContent: {post.content}")
            print("Draft created!")
        except Exception as e:
            print(f"An error occurred: {e}")

    def list_drafts(self):
        try:
            drafts = os.listdir(self.drafts_dir)
            return drafts
        except Exception as e:
            print(f"An error occurred: {e}")
            return []

    def read(self):
        try:
            title = input("Enter draft title: ")
            if not title:
                print("Title cannot be empty.")
                return
            filename = f"{self.drafts_dir}/{title.replace(' ', '_')}.txt"
            if not os.path.exists(filename):
                print("Draft not found.")
                return
            with open(filename, "r") as file:
                print(file.read())
        except Exception as e:
            print(f"An error occurred: {e}")

    def delete(self):
        try:
            title = input("Enter draft title: ")
            if not title:
                print("Title cannot be empty.")
                return
            filename = f"{self.drafts_dir}/{title.replace(' ', '_')}.txt"
            if not os.path.exists(filename):
                print("Draft not found.")
                return
            os.remove(filename)
            print("Draft deleted!")
        except Exception as e:
            print(f"An error occurred: {e}")

def main():
    manager = BlogManager()
    while True:
        try:
            print("\nWhat would you like to do?")
            print("\n1. Create Draft")
            print("2. List Drafts")
            print("3. Read Draft")
            print("4. Delete Draft")
            print("5. Quit")
            choice = input("Choose: ")
            if choice == "1":
                manager.create()
            elif choice == "2":
                drafts = manager.list_drafts()
                if drafts:
                    print("\nThis are the available posts")
                    for index, draft in enumerate(drafts, 1):
                        print(f"{index}. {draft.replace('.txt', '').replace('_', ' ')}")
                else:
                    print("No drafts found.")
            elif choice == "3":
                manager.read()
            elif choice == "4":
                manager.delete()
            elif choice == "5":
                print("Exited successfully")
                break
            else:
                print("Invalid choice.")
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
    