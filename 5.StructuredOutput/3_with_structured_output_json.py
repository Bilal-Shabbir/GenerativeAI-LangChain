from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional, Literal
from pydantic import BaseModel, Field

load_dotenv()

model = ChatOpenAI(model='gpt-4o-2024-08-06')

# schema
json_schema = {
  "title": "Review",
  "type": "object",
  "properties": {
    "key_themes": {
      "title": "Key Themes",
      "description": "Write down the key themes discussed int the review in a list",
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "summary": {
      "title": "Summary",
      "description": "A brief summary of the review",
      "type": "string"
    },
    "sentiment": {
      "title": "Sentiment",
      "description": "Return sentiment of the review either negative, positive",
      "allOf": [
        {
          "$ref": "#/definitions/Literal-Pos-Neg"
        }
      ]
    },
    "pros": {
      "title": "Pros",
      "description": "Write down pros inside a list",
      "default": None,
      "type": [
        "array",
        "null"
      ],
      "items": {
        "type": "string"
      }
    },
    "cons": {
      "title": "Cons",
      "description": "Write down cons inside a list",
      "default": None,
      "type": [
        "array",
        "null"
      ],
      "items": {
        "type": "string"
      }
    },
    "name": {
      "title": "Name",
      "description": "Write the name of riviewr",
      "default": None,
      "type": [
        "string",
        "null"
      ]
    }
  },
  "required": [
    "key_themes",
    "summary",
    "sentiment"
  ],
  "definitions": {
    "Literal-Pos-Neg": {
      "title": "Literal-Pos-Neg",
      "enum": [
        "Pos",
        "Neg"
      ]
    }
  }
}


annotated_model = model.with_structured_output(json_schema)

result = annotated_model.invoke("""5.0 out of 5 stars - A True Flagship Experience Worth the Upgrade

Reviewed in the United States on November 10, 2025
Verified Purchase

I recently upgraded to the Apex X1 after using my previous phone for over three years, and the difference is night and day. This is the first phone in a long time that truly feels like a generational leap, not just a minor refresh.

The camera system is the star of the show. The low-light performance is absolutely stunning, capturing detail and color that I previously thought impossible on a smartphone. The new telephoto lens is fantastic for portraits and getting closer to the action without losing quality.

The display is vibrant, incredibly bright, and the adaptive 120Hz refresh rate makes scrolling and gaming buttery smooth. It’s a joy to look at. The new chip inside handles everything I throw at it—heavy gaming, complex photo editing, and multitasking—with zero lag or stuttering.

Battery life is strong, easily lasting me a full day of moderate to heavy use, something my old phone struggled with. And when it is time to charge, the fast charging capability gets me back to 80% in well under an hour.

It's a premium device with a premium price tag, but if you prioritize camera quality, processing power, and a world-class display, the Apex X1 delivers.

Pros:

Best-in-class camera performance, especially in low light

Stunning, bright, and smooth 120Hz adaptive display

Exceptional processing power and speed

Reliable all-day battery life with very fast charging

Cons:

High price point, making it a significant investment

The phone is quite large, which may be difficult for one-handed use

The charger is not included in the box (standard practice now, but still annoying)

I highly recommend this phone to anyone looking for the ultimate mobile experience.""")
print('--------------')
print(result)