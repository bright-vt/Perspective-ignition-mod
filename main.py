# Import the necessary modules
from perspective import PerspectiveApp, PerspectiveTable, PerspectiveViewer, PerspectiveButton
from perspective import PluginConfiguration, PluginConfigurationBuilder, PluginConfigurationType

# Define the password
correct_password = "password123"

# Define the function to check the password
def check_password(password):
    if password == correct_password:
        return True
    else:
        return False

# Create a Perspective App
app = PerspectiveApp()

# Create a Perspective Button
button = PerspectiveButton("Open Popup")

# Define the function to open the popup
def open_popup():
    # Create a Perspective Table to hold the popup content
    table = PerspectiveTable()

    # Create a password input field
    password_field = table.add_input("password", "Password", "password")

    # Create a button to submit the password
    submit_button = table.add_button("Submit")

    # Define the function to handle the submit button click
    def submit_password():
        password = password_field.get_value()
        if check_password(password):
            button.set_enabled(True)  # Enable the button
        else:
            app.close_popup()  # Close the popup

    # Bind the submit_password function to the submit button click event
    submit_button.on_click(submit_password)

    # Open the popup with the table content
    app.open_popup(table)

# Bind the open_popup function to the button click event
button.on_click(open_popup)

# Add the button to the app
app.add(button)

# Run the app
app.run()