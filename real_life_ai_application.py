import subprocess
import sys

# Function to install a package if it's not already installed
def install_textblob():
    try:
        from textblob import TextBlob
    except ModuleNotFoundError:
        print("Installing TextBlob...")
        subprocess.check_call([sys.executable, "-m", "ensurepip", "--upgrade"])
        subprocess.check_call([sys.executable, "-m", "pip", "install", "textblob"])
        from textblob import TextBlob
    return TextBlob

# Import TextBlob
TextBlob = install_textblob()

def analyze_sentiment(text):
    """Analyze the sentiment of the given text."""
    # Create a TextBlob object
    blob = TextBlob(text)
    
    # Get the sentiment polarity: -1 (negative) to 1 (positive)
    sentiment = blob.sentiment.polarity
    
    # Print the result
    if sentiment > 0:
        print(f"Positive sentiment: '{text}'")
    elif sentiment < 0:
        print(f"Negative sentiment: '{text}'")
    else:
        print(f"Neutral sentiment: '{text}'")

# Example texts
texts = [
    "I love this product, it works great!",
    "I hate waiting in long lines at the store.",
    "The weather is okay today."
]

# Analyze the sentiment of each text
for text in texts:
    analyze_sentiment(text)
