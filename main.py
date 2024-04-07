import streamlit as st
import ollama

# Streamlit app to input filenames and identify music stems
def main():
    st.title('Music Stem Identifier')

    # Text area for user input
    user_input = st.text_area("Enter the music file names, each one on a new line:", "")

    # Button to run the Ollama model
    if st.button('Identify Stems'):
        if user_input:  # Check if the user has entered any text
            filenames = user_input.split('\n')  # Split the input by new lines into a list
            filenames = [name.strip() for name in filenames if name.strip()]  # Remove any extra whitespace

            prompt = f"Given these music file names, identify the specific stem each represents. \
            Format your response by pairing the file name with the stem, without altering the original stem name. \
            Here are the files: {filenames}. Make sure to format the answer with only filename = instrument(s) you identified, don't write anything else. Your guess must be included in the filename, like don't come up with an instrument that is not in the filename"

            # Call the ollama generate function
            output = ollama.generate(model="mistral", prompt=prompt, stream=True)

            # Concatenate and display the responses as a single block
            full_response = ''.join(chunk["response"] for chunk in output)
            st.text(full_response)
        else:
            st.error("Please enter at least one filename.")

if __name__ == '__main__':
    main()
