from vector_store import save_to_store

version = "chapter1_v1"
with open("final_outputs/version_1.txt", "r", encoding="utf-8") as file:
    content = file.read()

metadata = {
    "status": "final",
    "reviewed_by": "human"
}

save_to_store(version, content, metadata)

