from deepseek import DeepSeek
from deepseek import DeepSeekAPI

# Sample documents for indexing
documents = [
    "The sky is blue and the sun is shining.",
    "Python is a programming language that is widely used for web development.",
    "Deep learning is a subset of machine learning focused on neural networks.",
    "DeepSeek allows you to perform semantic search across large datasets.",
    "AI is revolutionizing various fields including healthcare and finance."
]

# Initialize the DeepSeek instance
deepseek = DeepSeek()

# Index the documents
deepseek.index(documents)

# User's speech-to-text result (this is just an example)
user_query = "What is deep learning?"

# Perform semantic search using DeepSeek
results = deepseek.search(user_query)

# The results will contain the best matching document(s)
if results:
    print("Top search result:", results[0])  # First result will be the most relevant
else:
    print("No results found.")
