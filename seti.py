#
# Title: SETI Stations Radio Search Platform
# Description: Software for use with a radio telescope.
# Authors: Scott Carter seti@22u.ca
# Date: Saturday, December 14, 2024
# Version: 0.3
#

import tkinter

# Create main panel
main_window = tkinter.Tk()
main_window.withdraw() # Hide the window
main_window.geometry("600x600+100+100")
main_window.title("SETI Stations Search Platform")

# Add main_window to the auth frame
main_frame = tkinter.Frame(master=main_window)
main_frame.pack(pady=20, padx=60, fill="both", expand=False)

# Display the title
main_label_title = tkinter.Label(main_window, text="SETI Stations Search Platform", font=("Ariel", 18, 'bold'))
main_label_title.pack(pady=5, padx=10)

# Create authentication panel
auth_window = tkinter.Tk()
auth_window.geometry("500x265")
auth_window.title("SETI Stations Search Platform")

# Login function
def login():
    if user_field.get()=="username@22u.ca" and pass_field.get()=="123":
        print("Login Successful!")
        main_window.deiconify() # Display main application panel
        auth_window.destroy() # Destroy auth panel
    else:
        print("Username or Password Incorrect!")

# Add auth_window to the auth frame
auth_frame = tkinter.Frame(master=auth_window)
auth_frame.pack(pady=20, padx=60, fill="both", expand=False)

# Display the title
label = tkinter.Label(auth_window, text="SETI Stations Search Platform", font=("Ariel", 18, 'bold'))
label.pack(pady=5, padx=10)

# Username field
user_field = tkinter.Entry(auth_window, width="24")
user_field.insert(0,'username@22u.ca')
user_field.pack(pady=5, padx=10)

# Password field
pass_field = tkinter.Entry(auth_window, show="*", width="24")
pass_field.insert(0,'Password')
pass_field.pack(pady=5, padx=10)

# Display URL for further information
label_footer = tkinter.Label(auth_window, text="https://22u.ca/seti", font=("Ariel", 10, 'bold'))
label_footer.pack(pady=5, padx=10)

# Display the login button and run the login function when clicked
button = tkinter.Button(auth_window, text="Login", command=login)
button.pack(pady=12, padx=10)

# Start the authentication window
auth_window.mainloop()

# Hide the main_window if it is visible
main_window.withdraw()

# Run the main_window code
main_window.mainloop() 
