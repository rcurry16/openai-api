## OpenAI - API Usage

### Description
Exploring the capabilities of the OpenAI API. The api_usage.py file contains three basic functions that demonstrate the usage of various tools provided by OpenAI.

### Usage Instructions
- **API Key**
  - Obtain an API Key from OpenAI
  - Add your API Key to the 'api_usage.py' file
    
- **Text-to-Speech Function**
  - To use the text-to-speech function, you must define a file path where the generated MP3 will be saved

- **Speech-to-Text Function**
  - To use the speech-to-text function, you must define a file path where the audio filed will be retrieved from

### Examples 
- **text_gen(*input*)**
  - Example: text_gen('Where is coffee from?')
  - Output format: Prints the response
  - Note: This function doesn't maintain context
    
- **image_gen(*input*)**
  - Example: image_gen('a black cat drinking coffee')
  - Output format: Prints a link to the generated image
  - Note: The image URL is only active for 1 hour
    
- **voice_gen(*input*, *filename*)**
  - Example: voice_gen('Hello, I would like to drink coffee', 'coffee')
  - Output format: Saves as an mp3
  - Note: There are other voice options in the documentation

- **transcript_gen(*filepath*)**
  - Example: transcript_gen('/Users/username/Desktop/audiofile.mp3')
  - Output format: Prints the transcribed text
  - Note: The are multiple response format options, text is currently chosen

### Useful Links
- [OpenAI API Documentation](https://platform.openai.com/docs/overview)
- [API Usage](https://platform.openai.com/usage)