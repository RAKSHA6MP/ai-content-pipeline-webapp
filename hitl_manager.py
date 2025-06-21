import os
import json
import subprocess
import shutil

REVISION_LOG_PATH = "revisions/revision_log.json"

def read_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def write_file(path, content):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

def log_revision(version, feedback, action):
    if os.path.exists(REVISION_LOG_PATH):
        with open(REVISION_LOG_PATH, "r", encoding="utf-8") as f:
            logs = json.load(f)
    else:
        logs = []

    logs.append({
        "version": version,
        "ai_writer": "Gemini (via ai_writer.py)",
        "human_feedback": feedback,
        "action_taken": action
    })

    with open(REVISION_LOG_PATH, "w", encoding="utf-8") as f:
        json.dump(logs, f, indent=2)

def generate_ai_version(version_num):
    print("🚀 Running ai_writer.py to generate content with Gemini...")
    subprocess.run(["python", "ai_writer.py"], check=True)

    src = "rephrased_text.txt"
    dest = f"final_outputs/version_{version_num}.txt"

    if os.path.exists(src):
        shutil.copy(src, dest)
        print(f"✅ AI Version {version_num} saved to {dest}")
        return read_file(dest)
    else:
        raise FileNotFoundError("rephrased_text.txt not found after running ai_writer.py")

def human_review_loop():
    version = 1
    while True:
        version_path = f"final_outputs/version_{version}.txt"
        if not os.path.exists(version_path):
            ai_output = generate_ai_version(version)
        else:
            ai_output = read_file(version_path)

        print(f"\n📝 Reviewing Version {version}...\n")
        print("--- AI Generated Content Preview ---\n")
        print(ai_output[:500])

        decision = input("\nDo you want to (a)ccept, (e)dit, (r)eject and regenerate, or (i)nstruct Gemini to revise? ").strip().lower()

        if decision == 'a':
            print("✅ Content approved.")
            write_file("final_outputs/final_version.txt", ai_output)
            log_revision(version, "Looks good", "Accepted")
            break

        elif decision == 'e':
            print("✏️ Paste your manually edited version below:")
            edited = input("\nYour edited content:\n")
            write_file(f"final_outputs/edited_{version}.txt", edited)
            write_file("final_outputs/final_version.txt", edited)
            log_revision(version, "Manually edited by human", "Accepted with human edits")
            break

        elif decision == 'i':
            instruction = input("🧠 Enter your instruction to Gemini (e.g., 'Make it more technical'):\n")
            instruct_prompt = f"Here is a paragraph:\n\n{ai_output}\n\nRewrite it based on this instruction: {instruction}"

            from ai_writer import generate_ai_text
            new_text = generate_ai_text(instruct_prompt)

            version += 1
            new_path = f"final_outputs/version_{version}.txt"
            write_file(new_path, new_text)
            log_revision(version, f"Instructed: {instruction}", "Generated new version using instruction")
            print(f"✅ New version {version} generated based on your instruction.\n")

        elif decision == 'r':
            log_revision(version, "Not good enough", "Rejected")
            version += 1
            print(f"\n🔁 Generating version {version}...")
        else:
            print("⚠️ Invalid input. Please choose 'a', 'e', 'r', or 'i'.")

if __name__ == "__main__":
    human_review_loop()