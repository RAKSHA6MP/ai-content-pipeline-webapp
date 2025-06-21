# vector_store.py

import os
import json
import torch

from sentence_transformers import SentenceTransformer, util

device = "cuda" if torch.cuda.is_available() else "cpu"


# Load the model once globally
model = SentenceTransformer("all-MiniLM-L6-v2")

# Ensure the storage directory exists
STORE_DIR = "embeddings_store"
os.makedirs(STORE_DIR, exist_ok=True)

def save_to_store(doc_id, content, metadata):
    """Saves the document embedding and metadata into a local JSON file."""
    embedding = model.encode(content, convert_to_tensor=True).tolist()

    data = {
        "doc_id": doc_id,
        "content": content,
        "embedding": embedding,
        "metadata": metadata
    }

    with open(f"{STORE_DIR}/{doc_id}.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    print(f"✅ Saved: {STORE_DIR}/{doc_id}.json")


def search_versions(query, top_k=1, return_data=False):
    """Searches for the most relevant versions based on the query."""
    query_embedding = model.encode(query, convert_to_tensor=True)
    scores = []

    for file_name in os.listdir(STORE_DIR):
        if file_name.endswith(".json"):
            with open(os.path.join(STORE_DIR, file_name), "r", encoding="utf-8") as f:
                data = json.load(f)
                doc_embedding = torch.tensor(data["embedding"], device=device)

                score = util.pytorch_cos_sim(query_embedding, doc_embedding).item()
                scores.append((file_name, score, data["content"][:200]))

    # Sort by highest score
    scores.sort(key=lambda x: x[1], reverse=True)

    if return_data:
        return scores[:top_k]

    if not scores:
        print("❌ No stored versions found.")
        return

    print(f"\n🔍 Top {top_k} match(es):")
    for i in range(min(top_k, len(scores))):
        file, score, preview = scores[i]
        print(f"\n📄 {file} — Score: {score:.4f}")
        print(f"📝 Preview: {preview}...")
