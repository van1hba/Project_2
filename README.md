# Project_2
Multi-Timezone Desktop Clock
Overview
This project is a graphical clock application that displays real-time clocks for several major cities worldwide using the Tkinter library. Each timezone is represented by its own labeled clock, alongside a flag image, making it useful for tracking current time across continents in a visually appealing desktop layout.

Features
Displays Current Time for India, USA (New York), UK (London), and Japan (Tokyo) simultaneously.

Graphical Interface built with Tkinter, including customized window layout and embedded flag images for each country.

Regular Updates: Each clock refreshes every second for accurate timekeeping.

Dependencies
The following libraries must be installed and available in the Python environment:

tkinter (standard with Python)

datetime (standard with Python)

pytz (install via pip)

Install missing dependencies:

bash
pip install pytz
Required Images
The script references several PNG image files for clock icons and country flags. Place these files in the same directory as clock.py and ensure names match:

dokclock.png

dokind.png

dokusa.png

dokeng.png

dokjap.png

Usage
Run the application from the terminal or your IDE:

bash
python clock.py
A window will appear displaying clocks for each country. The GUI is sized to 1200x600 pixels for visibility.

Customization
Add more timezones by duplicating the corresponding code blocks and updating their settings.

Update flag images as desired, ensuring filenames match those used in the script.

Author and License
The script does not specify an author or license information.

This README guides users in setting up and running the multi-timezone clock application, including dependencies and image requirements for proper display.
