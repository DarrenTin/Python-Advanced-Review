from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from textblob import TextBlob

def analyze_sentiment(text, method="vader"):
    """
    Analyzes sentiment of a given text using VADER or TextBlob.
    
    :param text: Input text for sentiment analysis.
    :param method: 'vader' for short texts, 'textblob' for general analysis.
    :return: Sentiment category (Positive, Neutral, Negative) and score.
    """
    
    if not text.strip():
        return "❌ Error: Empty text input!"

    if method == "vader":
        analyzer = SentimentIntensityAnalyzer()
        score = analyzer.polarity_scores(text)["compound"]
    elif method == "textblob":
        score = TextBlob(text).sentiment.polarity
    else:
        return "❌ Error: Invalid method! Choose 'vader' or 'textblob'."

    # Determine sentiment category
    sentiment = "Neutral"
    if score > 0.05:
        sentiment = "Positive"
    elif score < -0.05:
        sentiment = "Negative"

    return f"📝 Sentiment: {sentiment} | Score: {score:.2f}"

# Main program
if __name__ == "__main__":
    print("📊 NLP Sentiment Analyzer 📊")

    user_text = input("Enter a sentence or paragraph to analyze: ").strip()
    method_choice = input("Choose method ('vader' for short text, 'textblob' for general analysis, default: vader): ").strip().lower() or "vader"

    result = analyze_sentiment(user_text, method_choice)
    print("\n" + result)
