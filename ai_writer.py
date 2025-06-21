import os
import google.generativeai as genai

genai.configure(api_key="AIzaSyBsuXf6ue0uW_0dpfY-zDSyP69x1ReaU4o")


def generate_ai_text(input_text):
    model = genai.GenerativeModel("models/gemini-1.5-flash")
    response = model.generate_content(f"Rewrite the following chapter in clearer and modern English:\n\n{input_text}")
    return response.text.strip()

if __name__ == "__main__":
    with open("inputs/original_text.txt", "r", encoding="utf-8") as file:
        original_text = file.read()

    new_text = generate_ai_text(original_text)

    os.makedirs("final_outputs", exist_ok=True)
    with open("final_outputs/version_1.txt", "w", encoding="utf-8") as f1:
        f1.write(new_text)

    with open("rephrased_text.txt", "w", encoding="utf-8") as f2:
        f2.write(new_text)

    print("✅ Rewritten chapter saved to final_outputs/version_1.txt and rephrased_text.txt")

