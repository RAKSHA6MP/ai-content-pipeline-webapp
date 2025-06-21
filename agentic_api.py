from ai_writer import generate_ai_text
from vector_store import save_to_store
import os



def writer_agent(text):
    return generate_ai_text(text)

def reviewer_agent(text):
    return generate_ai_text(text)

def run_pipeline():
    with open("inputs/original_text.txt", "r", encoding="utf-8") as file:
        content = file.read()

    print("📝 Running Writer Agent...")
    rewritten = writer_agent(content)

    print("🔍 Passing to Reviewer Agent...")
    reviewed = reviewer_agent(rewritten)

    os.makedirs("final_outputs", exist_ok=True)
    with open("final_outputs/final_version.txt", "w", encoding="utf-8") as f:
        f.write(reviewed)

    save_to_store("final_version", reviewed, metadata={"status": "final", "flow": "agentic"})
    print("✅ Agentic pipeline complete and saved.")

if __name__ == "__main__":
    run_pipeline()