from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional, Literal

load_dotenv()

model = ChatOpenAI()

class Review(TypedDict):
    summary : str
    sentiment: str


structured_model = model.with_structured_output(Review)

result = structured_model.invoke("""I held off buying one of these for years, thinking, "How much better can an insulated bottle be?" Well, let me tell you, this HydroFlask has converted me completely. It's not just a water bottle; it's a trusty piece of gear that has genuinely improved my hydration habits.""")

print(result)

# analysing result we can see summary is generated although we did not give prompt. It is due to fact that in when we use with_structured_output, a prompt is created behind the scene 

# Sometime llm may not understand from dict so we can use Annotated

class AnnotatedReview(TypedDict):
    # only for representation, not for validation
    key_themes: Annotated[list[str], 'Write down the key themes discussed int the review in a list']
    summary : Annotated[str, 'A brief summary of the review'] 
    sentiment: Annotated[Literal['Pos', 'Neg'], 'Return sentiment of the review either negative, positive or neutral']
    pros: Annotated[Optional[list[str]], 'Write down pros inside a list']
    cons: Annotated[Optional[list[str]], 'Write down cons inside a list']
    name: Annotated[Optional[list[str]], 'Write the name of riviewr']


annotated_model = model.with_structured_output(AnnotatedReview)

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