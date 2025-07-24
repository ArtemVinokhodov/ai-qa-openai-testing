# 🧪 AI Prompt Testing Framework

This project demonstrates automated prompt testing for various OpenAI models (e.g., `gpt-3.5-turbo`, `gpt-4.1-nano`). It evaluates AI responses based on tone, accuracy, translation, and formatting.

## ✅ Features

* Load test cases from code
* Execute prompts with specified tone and model
* Store results in `test_results.csv`
* Basic Pass/Fail validation with comments

## 📁 Files

* `test_prompt_api.py` — main test runner
* `test_results.csv` — output log of test cases
* `.env` — your OpenAI API key
* `requirements.txt` — dependencies

## 🧪 Sample Test Cases

Below is a preview of test results:

| Prompt                                   | Tone   | Model        | Output                            | Pass | Comment |
| ---------------------------------------- | ------ | ------------ | --------------------------------- | ---- | ------- |
| Write a polite email to cancel a meeting | polite | gpt-4.1-nano | "Subject: Cancellation..."        | ✅    | OK      |
| Translate into Polish: I can't attend    | polite | gpt-4.1-nano | Nie mogę uczestniczyć w spotkaniu | ✅    | OK      |
| Make this short: I'm sorry, I can't come | short  | gpt-4.1-nano | Sorry, I can't make it.           | ✅    | OK      |

👉 See all test results in [`test_results.csv`](test_results.csv)

## 🧰 Setup

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```
OPENAI_API_KEY=your_api_key_here
```

Run tests:

```bash
python test_prompt_api.py
```

## 💡 Use Case

This project is useful for:

* Testing prompt stability
* Verifying multilingual output
* Experimenting with tone-based prompt engineering
* AI QA portfolios

---
