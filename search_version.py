# search_version.py

from vector_store import search_versions

query = input("🔎 Enter your search query: ")
search_versions(query, top_k=3)
