# Chroma DB Operations Lab

## Overview
The Chroma DB Operations Lab is designed to provide a comprehensive guide to essential database operations using Chroma DB. This project includes functionalities for creating collections, managing documents, and performing similarity searches on vector embeddings.

## Project Structure
```
chroma-db-ops-lab
├── src
│   ├── main.py                  # Entry point for the application
│   ├── chroma_client.py         # Handles connection to Chroma DB
│   └── operations
│       ├── collections.py       # Functions for managing collections
│       ├── documents.py         # Functions for managing documents
│       └── similarity_search.py  # Functions for performing similarity searches
├── data
│   └── employees.json           # Employee dataset for testing
├── notebooks
│   └── essential_database_operations.ipynb  # Jupyter notebook for hands-on guide
├── requirements.txt             # Project dependencies
└── README.md                    # Project documentation
```

## Setup Instructions
1. Clone the repository:
   ```
   git clone <repository-url>
   cd chroma-db-ops-lab
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Ensure you have access to Chroma DB and configure any necessary environment variables.

## Usage
- To run the application, execute the following command:
  ```
  python src/main.py
  ```

- For a hands-on experience with essential database operations, open the Jupyter notebook located in the `notebooks` directory:
  ```
  jupyter notebook notebooks/essential_database_operations.ipynb
  ```

## Functionality
- **Creating Collections**: Use the `create_collection` function in `collections.py` to create new collections in Chroma DB.
- **Managing Documents**: Add, modify, and retrieve documents using the functions provided in `documents.py`.
- **Similarity Searches**: Perform similarity searches on vector embeddings with the `perform_similarity_search` function in `similarity_search.py`.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.