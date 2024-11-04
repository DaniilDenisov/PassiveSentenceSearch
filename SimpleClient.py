import tkinter as tk
import requests
from tkinter import messagebox

# Function to send POST request to the Flask API
def send_text():
    user_input = text_entry.get("1.0", tk.END).strip()  # Get text input from the Tkinter text widget
    if not user_input:
        messagebox.showwarning("Input Error", "Please enter some text.")
        return
    
    url = 'http://127.0.0.1:5000/get_passive_sentences'
    data = {'text': user_input}

    try:
        # Try sending the POST request
        response = requests.post(url, json=data)

        # Raise an exception for bad HTTP status codes (e.g., 404, 500)
        response.raise_for_status()

        # Parse the JSON response
        response_data = response.json()

        # Display the result in a message box
        text_entry.delete("1.0", tk.END)  # Clear the text widget
        result = f"Passive sentences:\n{response_data}"
        text_entry.insert("1.0", result)  # Insert the result into the text widget

    except requests.exceptions.ConnectionError:
        # Handle the case where the server is not running
        messagebox.showerror("Connection Error", "Could not connect to the server. Please ensure the server is running.")
    
    except requests.exceptions.HTTPError as http_err:
        # Handle specific HTTP error responses (e.g., 404, 500)
        messagebox.showerror("HTTP Error", f"HTTP error occurred: {http_err}")
    
    except requests.exceptions.RequestException as req_err:
        # Catch all other request exceptions (timeout, too many redirects, etc.)
        messagebox.showerror("Error", f"An error occurred: {req_err}")

# Create the main Tkinter window
root = tk.Tk()
root.title("Passive Sentence Search")

# Create a label
label = tk.Label(root, text="Enter text to analyze for passive voice:")
label.pack(pady=10)

# Create a text box for user input
text_entry = tk.Text(root, height=10, width=50)
text_entry.pack(pady=10)

# Create a button to send the text input
send_button = tk.Button(root, text="Submit", command=send_text)
send_button.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
