# AI Essay Feedback System using LangGraph

An AI-powered essay evaluation system built with **LangGraph**, **LangChain**, and **Groq LLMs**. The application uses multiple AI agents to analyze essays from different perspectives and generate detailed feedback along with an overall evaluation report.

## Features

* Multi-agent architecture using LangGraph
* Parallel essay evaluation
* Grammar and language assessment
* Critical analysis evaluation
* Clarity and readability assessment
* Overall score calculation
* Comprehensive feedback report generation
* Powered by Groq's Llama models

## Architecture

```text
                START
                   |
                   v

                Essay

         /         |         \

        /          |          \

 Language     Analysis     Clarity

        \          |          /

         \         |         /

          Aggregate Scores

                  |
                  v

              Final Report
```

### Agents

#### Language Agent

Evaluates:

* Grammar
* Vocabulary
* Sentence Structure

#### Analysis Agent

Evaluates:

* Critical Thinking
* Depth of Analysis
* Quality of Arguments

#### Clarity Agent

Evaluates:

* Readability
* Organization
* Clarity of Ideas

#### Aggregator Agent

* Collects results from all agents
* Calculates overall score
* Generates final evaluation report

## Tech Stack

* Python
* LangGraph
* LangChain
* Groq API
* Llama 3.3 70B Versatile
* dotenv

## Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/essay-feedback-system.git

cd essay-feedback-system
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

Mac/Linux:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
```

## Run Project

```bash
python main.py
```

## Example Input

```text
Artificial Intelligence is transforming industries across the world.
It helps businesses automate repetitive tasks and improve efficiency.
```

## Example Output

```text
Language Score: 8/10

Analysis Score: 7/10

Clarity Score: 9/10

Average Score: 8.0/10
```

## Learning Outcomes

This project demonstrates:

* LangGraph State Management
* Multi-Agent Systems
* Parallel Node Execution
* Workflow Orchestration
* Prompt Engineering
* LLM Integration
* Structured AI Feedback Generation

## Future Improvements

* Essay Improvement Agent
* PDF Upload Support
* Streamlit Web Interface
* Feedback History Storage
* Rubric-Based Evaluation
* Export Reports as PDF
* Multi-language Support

## Author

Sanket Mali

Computer Science & Business Systems Student | AI & Full-Stack Development Enthusiast
