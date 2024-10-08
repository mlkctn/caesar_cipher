How to Run the Program
1-Clone the Repository:

If you're using Git, clone the repository with:
git clone https://github.com/yourusername/caesar_cipher.git

Navigate to the project folder:
cd caesar_cipher

2-Run the Program:
To run the program directly with Python:

python cipher.py

The program will prompt you to enter:

Whether you want to encode or decode a message.
The message to be encoded or decoded.
The shift value (a number that indicates how many positions each letter will be shifted).

Creating an Executable with PyInstaller

Install PyInstaller:

pip install pyinstaller

Navigate to Your Project Directory:

cd path_to_your_directory/caesar_cipher

Create the Executable: Run the following command to package the script as a single executable file:

pyinstaller --onefile cipher.py

Locate the Executable: After the process is complete, you will find the executable in the dist/ folder:

On Windows: dist/cipher.exe
On macOS/Linux: dist/cipher

Run the Executable: You can now distribute this executable. Double-click (Windows) or run it from the terminal (macOS/Linux) to use the Caesar Cipher program without needing Python.

Contributing
If you'd like to contribute to this project, feel free to fork the repository and submit a pull request. Improvements such as adding a graphical user interface (GUI) or additional cipher methods are welcome!


