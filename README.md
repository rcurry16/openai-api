## OpenAI API Usage

### Description
Exploring the capabilities of the OpenAI API. The api_usage.py file contains three basic functions that demonstrate the usage of various tools provided by OpenAI.

### Usage Instructions
- **API Key**
  - Obtain an API Key from OpenAI
  - Add your API Key to the appropriate location in the 'api_usage.py' file
    
- **Text-to-Speech Function**
  - To use the text-to-speech function, you must define a file path where the generated MP3 will be saved

### Examples 
- **text_gen(*input*)**
  - text_gen('Where is coffee from?')
  - Output format: Prints the response
  - Note: This function doesn't maintain context
    
- **image_gen(*input*)**
  - image_gen('a black cat drinking coffee')
  - Output format: Prints a link to the generated image
  - Note: The image URL is only active for 1 hour
    
- **voice_gen(*input*, *filename*)**
  - voice_gen('Hello, I would like to drink coffee', 'coffee')
  - Output format: Saves as an mp3
  - Note: There are other voice options in the documentation

### Useful Links
- [OpenAI API Documentation](https://platform.openai.com/docs/overview)
