import tweepy

# Set your Twitter API keys and access tokens
API_KEY = "YOUR_API_KEY"
API_SECRET_KEY = "YOUR_API_SECRET_KEY"
ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
ACCESS_TOKEN_SECRET = "YOUR_ACCESS_TOKEN_SECRET"

# Authenticate with Twitter
auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

# Create an API object
api = tweepy.API(auth)

# Function to post a tweet
def post_tweet(tweet_text):
    try:
        api.update_status(tweet_text)
        print("Tweet posted successfully!")
    except tweepy.TweepError as e:
        print(f"Error posting tweet: {e.reason}")

# Example usage:
if __name__ == "__main__":
    tweet_text = "Hello, Twitter! This is a test tweet from my Python bot."
    post_tweet(tweet_text)
