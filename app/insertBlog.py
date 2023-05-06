from datetime import datetime
from pymongo import MongoClient

user = 'username'           # username as set for the mongodb admin server (the username used in secret.yaml - before base64 conversion)
password = 'password'       # password as set for the mongodb admin server (the password used in secret.yaml - before base64 conversion)
host = 'mongodb-service'    # service name of the mongodb admin server as set in the service for mongodb server
port = '27017'              # port number of the mongodb admin server as set in the service for mongodb server
conn_string = f'mongodb://{user}:{password}@{host}:{port}'

db = MongoClient(conn_string).blog

# Select the blog database and the posts collection
collection = db.posts

# Create a new post document to insert into the collection
post = {
    "title": "My first blog post",
    "author": "John Doe",
    "createdAt": datetime.utcnow()
}

# Insert the post document into the collection
result = collection.insert_one(post)

# Print the ID of the inserted document
print(f"Inserted post with ID {result.inserted_id}")
