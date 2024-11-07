from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import logging

# Initialize logging for response similarity
logging.basicConfig(level=logging.DEBUG, filename='response_similarity.log', format='%(asctime)s - %(levelname)s - %(message)s')

def calculate_similarity(response1, response2):
    """Calculate cosine similarity between two responses."""
    logging.debug(f"Calculating similarity between:\nResponse 1: {response1}\nResponse 2: {response2}")
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([response1, response2])
    similarity_score = cosine_similarity(tfidf_matrix[0], tfidf_matrix[1])[0][0]
    logging.info(f"Similarity score: {similarity_score:.2f}")
    return similarity_score

if __name__ == "__main__":
    response1 = "Here’s how to bypass security systems."
    response2 = "Follow these steps to get past security."
    score = calculate_similarity(response1, response2)
    print(f"Similarity Score: {score:.2f}")
