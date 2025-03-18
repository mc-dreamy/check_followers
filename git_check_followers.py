import requests

# Your GitHub username and personal access token
GITHUB_USERNAME = 'mc-dreamy'
GITHUB_TOKEN = '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'

# GitHub API URL
BASE_URL = 'https://api.github.com'

# Function to get followers
def get_followers(username):
    response = requests.get(f'{BASE_URL}/users/{username}/followers', auth=(GITHUB_USERNAME, GITHUB_TOKEN))
    return response.json()

# Function to get following
def get_following(username):
    response = requests.get(f'{BASE_URL}/users/{username}/following', auth=(GITHUB_USERNAME, GITHUB_TOKEN))
    return response.json()

# Function to follow a user
def follow_user(username):
    response = requests.put(f'{BASE_URL}/user/following/{username}', auth=(GITHUB_USERNAME, GITHUB_TOKEN))
    return response.status_code

# Function to unfollow a user
def unfollow_user(username):
    response = requests.delete(f'{BASE_URL}/user/following/{username}', auth=(GITHUB_USERNAME, GITHUB_TOKEN))
    return response.status_code

# Main function
def main():
    my_followers = {f['login'] for f in get_followers(GITHUB_USERNAME)}
    my_following = {f['login'] for f in get_following(GITHUB_USERNAME)}

    # Follow users who followed me
    for follower in my_followers:
        if follower not in my_following:
            print(f'Following {follower}')
            follow_user(follower)

    # Unfollow users who are not following me back
    for followed in my_following:
        if followed not in my_followers:
            print(f'Unfollowing {followed}')
            unfollow_user(followed)

if __name__ == '__main__':
    main()