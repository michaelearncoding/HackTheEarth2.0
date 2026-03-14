def create_collection(chroma_client, collection_name):
    """Create a new collection in Chroma DB."""
    try:
        chroma_client.create_collection(collection_name)
        print(f"Collection '{collection_name}' created successfully.")
    except Exception as e:
        print(f"Error creating collection: {e}")

def list_collections(chroma_client):
    """List all collections in Chroma DB."""
    try:
        collections = chroma_client.list_collections()
        return collections
    except Exception as e:
        print(f"Error listing collections: {e}")
        return []

def delete_collection(chroma_client, collection_name):
    """Delete a collection from Chroma DB."""
    try:
        chroma_client.delete_collection(collection_name)
        print(f"Collection '{collection_name}' deleted successfully.")
    except Exception as e:
        print(f"Error deleting collection: {e}")