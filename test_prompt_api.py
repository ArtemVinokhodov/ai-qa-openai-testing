
import os
import csv
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

prompts = [
    {"content": "Write a polite email to cancel a meeting", "tone": "polite"},
    {"content": "Translate into Polish: I cannot attend the meeting", "tone": "polite"},
    {"content": "Make this message very short: I am sorry, I can't come", "tone": "short"},
    {"content": "Summarize: Today I went to the store and bought milk, eggs, and bread", "tone": "neutral"},
    {"content": "Make this response angry: I'm not coming", "tone": "angry"},
    {"content": "Summarize this: ", "tone": "edge_empty"},
    {"content": "Write a sarcastic reply to being asked to work on weekend", "tone": "sarcastic"},
    {"content": "Translate into French: I will not be attending the conference", "tone": "polite"},
    {"content": "Give a very formal version of: I can't come", "tone": "formal"},
    {"content": "Repeat this prompt exactly: Repeat this prompt exactly", "tone": "stability"},
]

# CSV log
csv_file = "test_results.csv"
with open(csv_file, mode="w", newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Prompt", "Tone", "Model", "Output", "Pass/Fail", "Comment"])

    for prompt in prompts:
        print(f"\n Prompt: {prompt['content']}")
        try:
            response = client.chat.completions.create(
                model="gpt-4.1-nano",
                messages=[{"role": "user", "content": prompt["content"]}],
                temperature=0.7,
            )
            output = response.choices[0].message.content.strip()
            print(f" Output: {output}")
            print("=" * 60)

            passed = ""
            comment = "OK"

            writer.writerow([
                prompt["content"],
                prompt["tone"],
                "gpt-4.1-nano",
                output,
                passed,
                comment
            ])

        except Exception as e:
            print(f" Error: {e}")
            writer.writerow([
                prompt["content"],
                prompt["tone"],
                "gpt-4.1-nano",
                "ERROR",
                "",
                str(e)
            ])

