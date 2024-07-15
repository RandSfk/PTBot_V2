# PTBot_V2
A Simple ChatBot for Pony Town

## How To Use

### Installation

1. **Clone the Repository:** You can clone this repository using the following command:
   ```bash
   git clone https://github.com/RandSfk/PTBot_V2.git
   ```
   Or download the repository directly from the GitHub page.

2. **Setup Bot Configuration:**
   - Open `config.json` and change the settings to your preferences or keep the default settings.

3. **Do Not:**
   - Don't change the name of the `command.py` file.

### Usage

1. **Run the Bot:**
   - After completing the installation and configuration steps, run the bot script using:
     ```bash
     python main.py
     ```

### Wikis

1. **Setup Command:**
   - Ensure the `def command` is in `command.py`.
   - To receive whispers, make sure the `whisp` argument is set to `False` initially. If `whisp` is `True`, the function will return "You are receiving a whisper from {username}".

   ```python
   def command(username, args, whisp=False): #set to False so that the incoming chat is not a whisper
       roles = {
           'guest': {
               'menu|menus|help|m|h': f"Hello, {username}!",
               'about|owner': "This bot is owned by $owner."
           },
           'user': {
               'about|help': "$owner, $bot_name" #bot_info example
           },
           'admin': {
               'about': "Admins can manage the bot.",
               'moveUp|moveDown|moveLeft|moveRight': "Admins can move the bot using move commands."
           },
           'owner': {
               'about': "This bot is managed by the owner. Contact $owner for more details.",
               'moveUp': "Moves the bot up. Usage: 'moveUp(steps)'.",   #Use move commands with steps, e.g., moveUp(2)
               'moveDown': "Moves the bot down. Usage: 'moveDown(steps)'.",
               'moveLeft': "Moves the bot left. Usage: 'moveLeft(steps)'.",
               'moveRight': "Moves the bot right. Usage: 'moveRight(steps)'."
           }
       }

       bot_info = {
           '$bot_name': "Bot Name",
           '$owner': "Owner Name",
           '$bot_version': "Bot Version 1.0"
       }

       role = get_user_role(username)  # Assume a function that gets the role of the user

       if role in roles:
           for key in roles[role]:
               if args.split('(')[0] == key:
                   if 'steps' in roles[role][key]:
                       steps = args.split('(')[1].split(')')[0]
                       return format_output(roles[role][key].replace('(steps)', f'({steps})'))
                   else:
                       return format_output(roles[role][key])

       if args in bot_info:
           return format_output(bot_info[args])

       if whisp:  #For example, if you want to receive whisper messages
           return f"You are receiving a whisper from {username}"

       return "Command not found or not authorized."
   ```

### License

```
MIT License

Copyright (c) 2024 RandSfk

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
