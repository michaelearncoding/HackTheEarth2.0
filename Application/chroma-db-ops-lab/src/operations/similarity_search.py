def perform_similarity_search(chroma_client, collection_name, query_vector, top_k=5):
    """
    Perform a similarity search on the specified collection using the provided query vector.

    Parameters:
    - chroma_client: An instance of the ChromaClient to interact with the database.
    - collection_name: The name of the collection to search within.
    - query_vector: The vector representation of the query to find similar items.
    - top_k: The number of similar items to return (default is 5).

    Returns:
    - A list of documents that are similar to the query vector.
    """
    # Retrieve the collection from the Chroma DB
    collection = chroma_client.get_collection(collection_name)

    # Perform the similarity search
    similar_documents = collection.similarity_search(query_vector, top_k=top_k)

    return similar_documents

def main():
    # Example usage of the perform_similarity_search function
    from chroma_client import ChromaClient

    # Initialize the Chroma client
    client = ChromaClient()

    # Define the collection name and query vector
    collection_name = "employees"
    query_vector = [0.1, 0.2, 0.3]  # Example vector, replace with actual vector

    # Perform the similarity search
    results = perform_similarity_search(client, collection_name, query_vector)

    # Print the results
    for doc in results:
        print(doc)

if __name__ == "__main__":
    main()