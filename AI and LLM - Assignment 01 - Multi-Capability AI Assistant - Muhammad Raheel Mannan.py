"""
============================================================
🚀 PROJECT: Multi-Capability AI Assistant
============================================================

This assistant supports:
- Calculator
- Web Search
- Data Analysis
- Unit Conversion
- Weather Info
- Translation

Powered by OpenAI Function Calling
============================================================
"""

from openai import OpenAI
from dotenv import load_dotenv
import json
import os

# =========================
# SETUP
# =========================

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# 🎉 Welcome Message
print("\n" + "=" * 60)
print("Multi-Capability AI Assistant")
print("=" * 60)
print("System initializing...")
print("Loading tools and capabilities...")
print("Ready to serve!\n")


# =========================
# TOOLS IMPLEMENTATION
# =========================

def calculate(expression):
    try:
        return json.dumps({"result": eval(expression)})
    except:
        return json.dumps({"error": "Invalid expression"})


def web_search(query):
    results = {
        "ai trends": "Latest AI: Advanced reasoning, multimodal models",
        "technology": "Tech news: AI adoption accelerating",
        "email tips": "Email tips: Clear subject, concise content"
    }

    for k in results:
        if k in query.lower():
            return json.dumps({"results": results[k]})

    return json.dumps({"results": f"Info about {query}"})


def analyze_data(data_string, operation):
    data = json.loads(data_string)

    if operation == "sum":
        result = sum(data)
    elif operation == "average":
        result = sum(data) / len(data)
    elif operation == "max":
        result = max(data)
    elif operation == "min":
        result = min(data)
    else:
        result = None

    return json.dumps({"result": result})


# =========================
# UNIT CONVERTER
# =========================

def km_to_miles(v): return v * 0.621371
def miles_to_km(v): return v * 1.60934
def c_to_f(v): return v * 9/5 + 32
def f_to_c(v): return (v - 32) * 5/9
def kg_to_lbs(v): return v * 2.20462
def lbs_to_kg(v): return v * 0.453592
def kph_to_mph(v): return v * 0.621371
def mph_to_kph(v): return v * 1.60934


def convert_units(value, from_unit, to_unit):
    conversions = {
        ("km", "miles"): km_to_miles,
        ("miles", "km"): miles_to_km,
        ("celsius", "fahrenheit"): c_to_f,
        ("fahrenheit", "celsius"): f_to_c,
        ("kg", "lbs"): kg_to_lbs,
        ("lbs", "kg"): lbs_to_kg,
        ("kph", "mph"): kph_to_mph,
        ("mph", "kph"): mph_to_kph,
    }

    key = (from_unit.lower(), to_unit.lower())

    if key not in conversions:
        return json.dumps({"error": "Conversion not supported"})

    result = conversions[key](value)

    return json.dumps({
        "input": f"{value} {from_unit}",
        "output": f"{result} {to_unit}",
        "result": result
    })


# =========================
# WEATHER TOOL
# =========================

def get_weather(query):
    weather_data = {
        "karachi": "Karachi: 30°C, Sunny",
        "new york": "New York: 22°C, Cloudy",
        "london": "London: 18°C, Rainy"
    }

    for city in weather_data:
        if city in query.lower():
            return json.dumps({"weather": weather_data[city]})

    return json.dumps({"weather": f"Weather info for {query}"})


# =========================
# TRANSLATION TOOL
# =========================

def translate(text, target_language="spanish"):
    translations = {
        "spanish": {
            "hello": "hola",
            "world": "mundo",
            "good morning": "buenos días"
        },
        "french": {
            "hello": "bonjour",
            "world": "monde",
            "good morning": "bonjour"
        }
    }

    lang = target_language.lower()

    if lang not in translations:
        return json.dumps({"translation": "Language not supported"})

    for phrase in translations[lang]:
        if phrase in text.lower():
            return json.dumps({"translation": translations[lang][phrase]})

    return json.dumps({"translation": f"No match found"})


# =========================
# TOOL SCHEMAS
# =========================

calculator_tool = {
    "type": "function",
    "function": {
        "name": "calculate",
        "parameters": {
            "type": "object",
            "properties": {"expression": {"type": "string"}},
            "required": ["expression"]
        }
    }
}

web_search_tool = {
    "type": "function",
    "function": {
        "name": "web_search",
        "parameters": {
            "type": "object",
            "properties": {"query": {"type": "string"}},
            "required": ["query"]
        }
    }
}

data_analyzer_tool = {
    "type": "function",
    "function": {
        "name": "analyze_data",
        "parameters": {
            "type": "object",
            "properties": {
                "data_string": {"type": "string"},
                "operation": {"type": "string"}
            },
            "required": ["data_string", "operation"]
        }
    }
}

conversion_tool = {
    "type": "function",
    "function": {
        "name": "convert_units",
        "parameters": {
            "type": "object",
            "properties": {
                "value": {"type": "number"},
                "from_unit": {"type": "string"},
                "to_unit": {"type": "string"}
            },
            "required": ["value", "from_unit", "to_unit"]
        }
    }
}

weather_tool = {
    "type": "function",
    "function": {
        "name": "get_weather",
        "parameters": {
            "type": "object",
            "properties": {"query": {"type": "string"}},
            "required": ["query"]
        }
    }
}

translator_tool = {
    "type": "function",
    "function": {
        "name": "translate",
        "parameters": {
            "type": "object",
            "properties": {
                "text": {"type": "string"},
                "target_language": {"type": "string"}
            },
            "required": ["text"]
        }
    }
}


# =========================
# MULTI CAPABILITY AGENT
# =========================

class MultiCapabilityAssistant:

    def __init__(self):
        self.tools = [
            calculator_tool,
            web_search_tool,
            data_analyzer_tool,
            conversion_tool,
            weather_tool,
            translator_tool
        ]

        self.functions = {
            "calculate": calculate,
            "web_search": web_search,
            "analyze_data": analyze_data,
            "convert_units": convert_units,
            "get_weather": get_weather,
            "translate": translate
        }

        print("Multi-Capability Assistant Ready!")

    def use_tools(self, query):

        messages = [{"role": "user", "content": query}]

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            tools=self.tools
        )

        msg = response.choices[0].message

        if not msg.tool_calls:
            return msg.content

        messages.append(msg)

        for call in msg.tool_calls:
            name = call.function.name
            args = json.loads(call.function.arguments)

            result = self.functions[name](**args)

            messages.append({
                "role": "tool",
                "tool_call_id": call.id,
                "content": result
            })

        final = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages
        )

        return final.choices[0].message.content

    def process(self, request):
        print("\n" + "=" * 60)
        print("INPUT:", request)
        print("=" * 60)

        return self.use_tools(request)


# =========================
# RUN TESTS (UPDATED VERSION)
# =========================

if __name__ == "__main__":

    assistant = MultiCapabilityAssistant()

    print("\n" + "=" * 70)
    print("🚀 MULTI-CAPABILITY AGENT TEST SUITE")
    print("=" * 70)

    test_cases = {
        "🔄 UNIT CONVERSION TESTS": [
            "Convert 10 km to miles",
            "Convert 100 Celsius to Fahrenheit",
            "Convert 5 kg to lbs"
        ],

        "🧮 MATH TESTS": [
            "What is 25% of 160",
            "Calculate 12 * (5 + 3)"
        ],

        "🌤 WEATHER TESTS": [
            "weather in karachi",
            "weather in london"
        ],

        "🌐 TRANSLATION TESTS": [
            "translate hello to french",
            "translate good morning to spanish"
        ],

        "📊 DATA / ANALYTICS TESTS": [
            "average of [10, 20, 30, 40]",
            "max of [5, 99, 23, 1]"
        ]
    }

    for category, tests in test_cases.items():

        print("\n" + "=" * 70)
        print(category)
        print("=" * 70)

        for t in tests:

            print("\n🧪 INPUT:", t)

            try:
                response = assistant.process(t)
                print("\n💬 RESPONSE:", response)

            except Exception as e:
                print("❌ ERROR:", str(e))

            print("-" * 60)

    print("\n" + "=" * 70)
    print("✅ ALL TESTS COMPLETED")
    print("=" * 70)