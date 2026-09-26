# AI Finance Agent

An AI-powered finance agent built using **Agno**, **Groq**, **YFinance**, and **web search**.

The agent can research stock prices, analyst recommendations, company fundamentals, and other financial information using available financial and web search tools.

## Features

- AI-powered financial assistance
- Stock price information
- Analyst recommendations
- Company fundamentals
- Financial research using web search
- Real-time financial data through YFinance
- Markdown-formatted responses
- Built using Agno and Groq

## Architecture

```text
                    User Query
                        |
                        v
                +---------------+
                | Finance Agent |
                +-------+-------+
                        |
              +---------+---------+
              |                   |
              v                   v
        YFinance Tools       Web Search
              |                   |
              +---------+---------+
                        |
                        v
                  Groq AI Model
                        |
                        v
                   AI Response
```
## Technologies Used

- Python
- Agno
- Groq
- YFinance
- DuckDuckGo Web Search
- python-dotenv
- Streamlit

## Project Structure

```text
finance-agent/
|
├── finance.py
├── app.py
├── requirements.txt
├── .gitignore
└── .env
```
## Installation

Clone the repository:
```bash
git clone https://github.com/arishak10/finance-agent.git
cd finance-agent
```
Create a virtual environment:
```bash
python -m venv .venv
```
Activate the virtual environment on Windows:
```bash
.venv\Scripts\activate
```
Install the required packages:
```bash
pip install -r requirements.txt
```

## Environment Setup

Create a .env file in the project folder:
```bash
GROQ_API_KEY=your_groq_api_key
```
Replace your_groq_api_key with your own Groq API key.

Never upload your .env file or expose your API key publicly.

Run the Project

Start the Streamlit application:
```bash
streamlit run app.py
```
The application will open in your browser.

## Example Queries

Share the MSFT stock price and analyst recommendations.

What are the latest fundamentals of Apple?

Give me financial information about Tesla.

Compare the stock performance of Microsoft and Apple.

## Purpose

This project demonstrates how an AI agent can combine a large language model with financial data and web search tools to research and provide useful financial information.

## Author

 Arisha Khan
 
 Computer Science Student | AI/ML Enthusiast
