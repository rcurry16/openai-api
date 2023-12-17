# Required packages
# - openai
# - pathlib

# import packages
from openai import OpenAI
from pathlib import Path

# function to intialize client and set up api key - need to fix
def init_client():
  api_key ='enter-api-key-here'
  client = OpenAI(api_key=api_key)
  return client

# function to generate text using gpt-3.5-turbo
def text_gen(input):
  client = init_client()
  
  completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
      {"role": "system", "content": "You are helpful assistant. Answer the given questions."},
      {"role": "user", "content": input}
  ])
  
  print(completion.choices[0].message.content)

# function to generate text using dalle-3
def image_gen(input):
  client = init_client()

  response = client.images.generate(
  model="dall-e-3",
  prompt=input,
  size="1024x1024",
  quality="standard",
  n=1,
  style="vivid")

  image_url = response.data[0].url
  print(image_url)  

# function to generate text to speech, update filepath for personal use
def voice_gen(text, filename):
  client = init_client()
  speech_file_path = f"/Users/ryancurry/Desktop/{filename}.mp3"
  response = client.audio.speech.create(
    model="tts-1-hd",
    voice="onyx",
    input=text
)
  response.stream_to_file(speech_file_path)

# example function calls
# text_gen("Where does coffee come from?")
# image_gen("a black cat drinking coffee")
# voice_gen("Hello, I am calling you about your car warranty", "sample")

# output formats
# text_gen() - prints the response
# image_gen() - prints the URL 
# voice_gen() - saves an mp3 file
