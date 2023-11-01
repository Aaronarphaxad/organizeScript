# organizeScript

Python Script to organize files in a folder

**Organize Downloads Folder Script**

This Python script organizes files in your Downloads folder on your computer based on their file extensions. It moves files into appropriate subfolders within the Downloads directory.

**Usage:**

1. **Prerequisites:**

   - You need Python installed on your computer. If you don't have it, download and install it from [python.org](https://www.python.org/).

2. **Download the Script:**

   - Download the script file and save it on your computer.

3. **Edit the Downloads Folder Path:**

   - Open the script in a text editor.
   - Change the `downloads_folder` variable to the path of your Downloads folder. For example:
     ```
     downloads_folder = "/Users/yourusername/Downloads"
     ```

4. **Customize File Types and Folders:**

   - Customize the `file_types` dictionary to map file extensions to folder names. You can add or modify file extensions and folder names according to your preferences.
   - For example, `"jpg": "Images"` means `.jpg` files will be moved to the `Images` folder.

5. **Run the Script Locally:**

   - Open a terminal or command prompt.
   - Navigate to the directory containing the script using the `cd` command.
   - Run the script by entering:
     ```
     python script_filename.py
     ```
     Replace `script_filename.py` with the actual filename of the script.

6. **Set Up Cron Job (Mac Users):**

   - Open Terminal.
   - Edit your crontab by running `crontab -e`.
   - Add a line to schedule the script to run at specific intervals. For example, to run the script every day at 2 AM, add the following line:
     ```
     0 2 * * * /usr/bin/python3 /path/to/your/script_filename.py
     ```
     Replace `/usr/bin/python3` with the actual path to your Python 3 interpreter and `/path/to/your/script_filename.py` with the full path to your Python script.
   - Save and exit the editor (for mac/linux users use i to enter insert mode, esc to escape, and :wq to save and quit).

7. **Set Up Task Scheduler (Windows Users):**
   - Open Task Scheduler from the Start menu.
   - Click on "Create Basic Task..." in the right panel.
   - Follow the wizard to set the task name, trigger (daily), start time, and action (start a program).
   - Browse and select the Python executable (`python.exe`) as the program/script.
   - Add the full path to your Python script in the "Add arguments" field.
   - Complete the wizard to create the task.

Now, the script will automatically organize your Downloads folder according to the specified rules. Customize the file extensions and folder names as needed for your workflow.
