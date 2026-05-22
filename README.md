============================================================
🤖 Multi-Capability AI Assistant
============================================================

A Python-based AI assistant powered by OpenAI Function Calling.

It can perform multiple tasks using tools such as:
- Calculator
- Web Search
- Data Analysis
- Unit Conversion
- Weather Information
- Translation

============================================================
FEATURES
============================================================

🧮 Calculator
- Solve mathematical expressions

🔍 Web Search
- Returns predefined knowledge-based results

📊 Data Analysis
- Sum, Average, Max, Min operations on lists

🔄 Unit Converter
- km ↔ miles
- kg ↔ lbs
- Celsius ↔ Fahrenheit
- speed conversions

🌤 Weather Tool
- Weather lookup for selected cities

🌐 Translator
- Translate English phrases to Spanish or French

============================================================
PROJECT STRUCTURE
============================================================

main.py
README.md
requirements.txt
examples.txt
.env

============================================================
SETUP INSTRUCTIONS
============================================================

1. Install Python (3.8+)

2. Create virtual environment:
   python -m venv venv

3. Activate environment:
   Windows:
   venv\Scripts\activate

   Mac/Linux:
   source venv/bin/activate

4. Install dependencies:
   pip install -r requirements.txt

5. Add API Key in .env file:
   OPENAI_API_KEY=your_api_key_here

6. Run project:
   python main.py

============================================================
EXAMPLE COMMANDS
============================================================

Convert 10 km to miles
What is 25% of 160
weather in karachi
translate hello to french
average of [10, 20, 30, 40]

============================================================