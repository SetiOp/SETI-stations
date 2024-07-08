#
# Title: SETI League Search Platform - Project Capellan 2024
# Description: Software for use with a radio telescope.
# Authors: Scott Carter scarter@setileague.ca
# Date: Monday, July 8, 2024
# Version: 0.1
#

import tkinter

# Create main panel
main_window = tkinter.Tk()
main_window.withdraw() # Hide the window
main_window.geometry("600x600+100+100")
main_window.title("Project Capellan")

# Add main_window to the auth frame
main_frame = tkinter.Frame(master=main_window)
main_frame.pack(pady=20, padx=60, fill="both", expand=False)

# Display the title
main_label_title = tkinter.Label(main_window, text="SETI League Search Platform", font=("Ariel", 18, 'bold'))
main_label_title.pack(pady=5, padx=10)

# Create authentication panel
auth_window = tkinter.Tk()
auth_window.geometry("500x265")
auth_window.title("Project Capellan")

# Login function
def login():
    if user_field.get()=="username@setileague.ca" and pass_field.get()=="123":
        print("Login Successful!")
        main_window.deiconify() # Display main application panel
        auth_window.destroy() # Destroy auth panel
    else:
        print("Username or Password Incorrect!")

# Add auth_window to the auth frame
auth_frame = tkinter.Frame(master=auth_window)
auth_frame.pack(pady=20, padx=60, fill="both", expand=False)

# Display the title
label = tkinter.Label(auth_window, text="SETI League Search Platform", font=("Ariel", 18, 'bold'))
label.pack(pady=5, padx=10)

# Username field
user_field = tkinter.Entry(auth_window, width="24")
user_field.insert(0,'username@setileague.ca')
user_field.pack(pady=5, padx=10)

# Password field
pass_field = tkinter.Entry(auth_window, show="*", width="24")
pass_field.insert(0,'Password')
pass_field.pack(pady=5, padx=10)

# Display URL for further information
label_footer = tkinter.Label(auth_window, text="https://www.setileague.ca/capellan.html", font=("Ariel", 10, 'bold'))
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
