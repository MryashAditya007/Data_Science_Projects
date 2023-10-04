from textblob import TextBlob

# Sample text for sentiment analysis
text = "I love this product! It's amazing."

# Create a TextBlob object
blob = TextBlob(text)

# Perform sentiment analysis
sentiment_score = blob.sentiment.polarity

# Determine sentiment
if sentiment_score > 0:
    sentiment = "Positive"
elif sentiment_score < 0:
    sentiment = "Negative"
else:
    sentiment = "Neutral"

# Print the sentiment and sentiment score
print(f"Sentiment: {sentiment}")
print(f"Sentiment Score: {sentiment_score}")
