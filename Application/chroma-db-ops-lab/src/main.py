# Essential Database Operations in Chroma DB

from chroma_client import ChromaClient
from operations.collections import create_collection, list_collections
from operations.documents import add_document, update_document, get_document
from operations.similarity_search import perform_similarity_search

def main():
    # Initialize the Chroma DB client
    client = ChromaClient()

    # Create a collection for employee data
    collection_name = "employees"
    create_collection(client, collection_name)

    # List collections to verify creation
    collections = list_collections(client)
    print("Collections in Chroma DB:", collections)

    # Example employee data to add
    employee_data = {
        "id": 1,
        "name": "John Doe",
        "position": "Software Engineer",
        "department": "Engineering"
    }

    # Add a document to the collection
    add_document(client, collection_name, employee_data)

    # Retrieve and print the document
    document = get_document(client, collection_name, employee_data["id"])
    print("Retrieved Document:", document)

    # Update the document
    updated_data = {"position": "Senior Software Engineer"}
    update_document(client, collection_name, employee_data["id"], updated_data)

    # Perform a similarity search
    query = "Software Engineer"
    similar_results = perform_similarity_search(client, collection_name, query)
    print("Similar Results:", similar_results)

if __name__ == "__main__":
    main()