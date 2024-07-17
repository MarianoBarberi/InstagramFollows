# Read the followers and following JSON files
import json
import os

# Get the absolute path of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the absolute file path to followers_1.json
followers_file_path = os.path.join(script_dir, 'followers_1.json')

# Construct the absolute file path to following.json
following_file_path = os.path.join(script_dir, 'following.json')

# Read the followers_1.json file
with open(followers_file_path) as followers_file:
    followers_data = json.load(followers_file)

# Read the following.json file
with open(following_file_path) as following_file:
    following_data = json.load(following_file)

# Extract the list of users from the JSON data
followers = [user['string_list_data'][0]['value'] for user in followers_data]
following = [string_data['value'] for relationship in following_data['relationships_following'] for string_data in relationship['string_list_data']]
# print(followers)

# Find users who are in following but not in followers
not_followed_back = [user for user in following if user not in followers]

# Print the result
print("Users who are in following but not in followers:")
for user in not_followed_back:
    print(user)