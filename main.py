import requests
import os



def save_voice_file(textfile, voice_file):
    # Read the content of the text file
    try:
        with open(f"{textfile}.txt", "r") as file:
            text = file.read()
    except FileNotFoundError:
        print(f"File not found...Creating new {textfile}.txt file")
        with open(f"{textfile}.txt", "w") as file:
            add_sentence = input("What do you want to write in the file: ")
            file.write(add_sentence)
            text = add_sentence
    # API endpoint and API key
    voice_endpoint = "https://api.voicerss.org"
    API_KEY = os.environ.get('API_VOICE_KEY')

    # Parameters for the API request
    user_params = {
        "key": API_KEY,
        "src": text,
        "hl": "en-gb",
    }

    # Send a GET request to the API
    response = requests.get(voice_endpoint, params=user_params)

    # Check if the response is successful (status code 200)
    if response.status_code == 200:
        # Save the voice file
        with open(f"{voice_file}.mp3", "wb") as file:
            file.write(response.content)
            print("Voice file saved successfully.")
    else:
        # Print the error message if the response is not successful
        print("Error occurred:", response.text)


if __name__ == "__main__":
    # Get the names of the input text file and output voice file from the user
    textfile = input("Name of text file: ")
    voice_file = input("What do you want the voice file to be called: ")

    # Call the function to save the voice file
    save_voice_file(textfile, voice_file)
