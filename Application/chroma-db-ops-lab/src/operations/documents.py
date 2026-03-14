def add_document(collection, document):
    """Add a document to the specified collection."""
    collection.add(document)


def update_document(collection, document_id, updated_fields):
    """Update a document in the specified collection."""
    document = collection.get(document_id)
    if document:
        for key, value in updated_fields.items():
            document[key] = value
        collection.update(document)


def get_document(collection, document_id):
    """Retrieve a document from the specified collection."""
    return collection.get(document_id)