import base64
import vertexai
from vertexai.generative_models import GenerativeModel, Part, SafetySetting


def generate():
    vertexai.init(project="personal-website-395618", location="us-central1")
    model = GenerativeModel(
        "gemini-1.5-flash-002",
    )
    responses = model.generate_content(
        [video1, text1],
        generation_config=generation_config,
        safety_settings=safety_settings,
        stream=True,
    )

    for response in responses:
        print(response.text, end="")

video1 = Part.from_uri(
    mime_type="video/*",
    uri="https://youtu.be/xZr_uo0Dm5A",
)
# https://youtu.be/xZr_uo0Dm5A

text1 = """Extract all of the URL\'s from this video, and print JUST THE URL\'s one by one. Ensure each URL is properly formatted. For example, a url that reads \'xyz.com\' should be formatted as \'www.xyz.com\'."""

generation_config = {
    "max_output_tokens": 8192,
    "temperature": 0.1,
    "top_p": 0.95,
}

safety_settings = [
    SafetySetting(
        category=SafetySetting.HarmCategory.HARM_CATEGORY_HATE_SPEECH,
        threshold=SafetySetting.HarmBlockThreshold.OFF
    ),
    SafetySetting(
        category=SafetySetting.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,
        threshold=SafetySetting.HarmBlockThreshold.OFF
    ),
    SafetySetting(
        category=SafetySetting.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT,
        threshold=SafetySetting.HarmBlockThreshold.OFF
    ),
    SafetySetting(
        category=SafetySetting.HarmCategory.HARM_CATEGORY_HARASSMENT,
        threshold=SafetySetting.HarmBlockThreshold.OFF
    ),
]

generate()