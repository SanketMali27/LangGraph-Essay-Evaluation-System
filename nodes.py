import ast
import json
import re
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile"
)

def extract_json_object(text: str) -> str:
    text = text.strip()

    # Trim common markdown fences
    text = re.sub(r"^```(?:json)?\s*", "", text, flags=re.IGNORECASE)
    text = re.sub(r"\s*```$", "", text)

    start = text.find("{")
    if start == -1:
        raise ValueError(f"No JSON object found in response: {text!r}")

    depth = 0
    for index, char in enumerate(text[start:], start=start):
        if char == "{":
            depth += 1
        elif char == "}":
            depth -= 1
            if depth == 0:
                return text[start:index + 1]

    raise ValueError(f"Unbalanced JSON object in response: {text!r}")


def parse_json_response(text: str) -> dict:
    json_text = extract_json_object(text)

    try:
        return json.loads(json_text)
    except json.JSONDecodeError:
        try:
            return ast.literal_eval(json_text)
        except Exception as exc:
            raise ValueError(
                f"Failed to parse JSON response. Raw: {text!r}. Extracted: {json_text!r}. Error: {exc}"
            ) from exc

def aggregator(state):
    language = parse_json_response(state["language_result"])

    analysis = parse_json_response(state["analysis_result"])

    clarity = parse_json_response(state["clarity_result"])

    avg = (
        language["score"]
        + analysis["score"]
        + clarity["score"]
    ) / 3

    report = f"""ESSAY EVALUATION REPORT

================================

LANGUAGE SCORE: {language['score']}/10
Feedback:
{language['feedback']}

================================

ANALYSIS SCORE: {analysis['score']}/10
Feedback:
{analysis['feedback']}

================================

CLARITY SCORE: {clarity['score']}/10
Feedback:
{clarity['feedback']}

================================

AVERAGE SCORE: {avg:.2f}/10
"""

    return {
        "avg_score": avg,
        "final_report": report
    }

def language_evaluator(state):
    essay = state["essay"]

    prompt = f"""
    Evaluate this essay.

    Return ONLY valid JSON with no other text, and do not include any explanation, markdown, or code fences.

    Example output:
    {{
        "score": 7,
        "feedback": "Your feedback here"
    }}

    Focus on:
    1. Grammar
    2. Vocabulary
    3. Sentence Structure

    Essay:
    {essay}
    """

    response = llm.invoke(prompt)

    return {
        "language_result": response.content
    }

def analysis_evaluator(state):
    essay = state["essay"]

    prompt = f"""
    Evaluate this essay.

    Return ONLY valid JSON with no other text, and do not include any explanation, markdown, or code fences.

    Example output:
    {{
        "score": 7,
        "feedback": "Your feedback here"
    }}

    Focus on:
    1. Depth of analysis
    2. Critical thinking
    3. Quality of arguments

    Essay:
    {essay}
    """

    response = llm.invoke(prompt)

    return {
        "analysis_result": response.content
    }

def clarity_evaluator(state):
    essay = state["essay"]

    prompt = f"""
    Evaluate this essay.

    Return ONLY valid JSON with no other text, and do not include any explanation, markdown, or code fences.

    Example output:
    {{
        "score": 7,
        "feedback": "Your feedback here"
    }}

    Focus on:
    1. Clarity
    2. Readability
    3. Organization

    Essay:
    {essay}
    """

    response = llm.invoke(prompt)

    return {
        "clarity_result": response.content
    }