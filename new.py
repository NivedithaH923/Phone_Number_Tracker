import requests
import tkinter as tk
from tkinter import messagebox
from tkinter import Tk, Label, Button, Entry, PhotoImage
import webbrowser

def fetch_phone_details():
    # Get the phone number from the input field
    phone_number = entry_phone_number.get()

    # Replace any non-numeric characters in the phone number
    phone_number = ''.join(filter(str.isdigit, phone_number))

    # Check if the phone number is valid
    if not phone_number:
        messagebox.showerror("Error", "Please enter a valid phone number.")
        return

    # Replace 'YOUR_NUMVERIFY_API_KEY' with your actual NumVerify API key
    numverify_api_key = '3b5b5360ef4fa0bce86932218e26ced8'
    numverify_url = f"http://apilayer.net/api/validate?access_key={numverify_api_key}&number={phone_number}"

    try:
        # Make the NumVerify API request
        numverify_response = requests.get(numverify_url)
        numverify_data = numverify_response.json()

        # Extract information from the NumVerify API response
        if numverify_data.get('valid'):
            service_provider = numverify_data.get('carrier', 'N/A')
            country_name = numverify_data.get('country_name', 'N/A')
            location = numverify_data.get('location', 'N/A')
            validity = numverify_data.get('valid', 'N/A')
            line_type = numverify_data.get('line_type', 'N/A')

            # Display the information in the GUI
            result_text = f"Service Provider: {service_provider}\nCountry: {country_name}\nLocation: {location}\nValidity: {validity}\nLine Type: {line_type}"
            label_result.config(text=result_text)
        else:
            messagebox.showerror("Error", "Invalid phone number. Please try again.")

    except requests.exceptions.RequestException:
        messagebox.showerror("Error", "Unable to fetch phone number details. Please try again later.")


# Create the main application window
app = tk.Tk()
app.title("Phone Number Tracker")
label_phone_number = tk.Label(app, text="PHONE NUMBER TRACKER", font=("Times", 25), fg="red")
label_phone_number.place(x=430,y=200)
# Create GUI elements
label_phone_number = tk.Label(app, text="Enter Phone Number:", font=("Times", 20))
label_phone_number.place(x=520,y=250)

entry_phone_number = tk.Entry(app, font=("Times", 20))
entry_phone_number.place(x=500,y=300)

button_track = tk.Button(app, text="Track", command=fetch_phone_details,font=("Times", 15))
button_track.place(x=600,y=360)

label_result = tk.Label(app, text="",font=("Times", 15))
label_result.place(x=410,y=420)


app.mainloop()
