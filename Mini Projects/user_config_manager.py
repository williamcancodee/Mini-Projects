def add_setting(settings, new_setting):
    key, value = new_setting
    

    key = key.lower()
    value = value.lower()

    if key in settings:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    else:
        settings[key] = value
        return f"Setting '{key}' added with value '{value}' successfully!"

def update_setting(settings, new_setting):
    # 1. Unpack and lowercase (just like before)
    key, value = new_setting
    key = key.lower()
    value = value.lower()
    
    # 2. Check if the key exists
    if key in settings:
        settings[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"
    else:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

def delete_setting(settings, key):
    key = key.lower()
    
    if key in settings:
        del settings[key]
        return f"Setting '{key}' deleted successfully!"
    else:
        return f"Setting not found!"

def view_settings(settings):
    # 1. Check if the dictionary is empty
    if not settings:
        return "No settings available."

    # 2. Start the output string
    output = "Current User Settings:\n"

    # 3. Loop through the settings to format them
    for key, value in settings.items():
        # Capitalize the key and add the value, followed by a new line
        output += f"{key.capitalize()}: {value}\n"

    return output

test_settings={
    "theme":"dark",
    "Notifications":"enabled",
    "Volume":"High",


}