# Study Reminder

This project is a simple application developed in Python using the Tkinter library. The application presents a reminder with a personalized message and allows the user to confirm a specific action, which is executed via a predefined system command.

## Requirements

- Python 3.x
- Tkinter (usually included with Python)
- A `settings.json` file with the necessary configurations

## Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/your_username/study_reminder.git
    cd study_reminder
    ```

2. Ensure you have Python 3.x installed on your system.

3. Verify that the `settings.json` file is present in the root directory of the project. This file should have the following format:

    ```json
    {
        "message": ["Your reminder message here", "The confirmation phrase here"],
        "exe_path": "path/to/executable",
        "launch_product": "product_name"
    }
    ```

## Usage

1. Run the Python script:

    ```bash
    python study_reminder.py
    ```

2. A window will appear with the reminder message specified in `settings.json`.

3. Select "Yes" to confirm the action. You will be prompted to enter a confirmation phrase. If the phrase is correct, the command specified in `settings.json` will be executed.

4. Select "No" to close the application without performing any action.

## Code Structure

- **center_window(window, width_percentage, height_percentage)**: Function to center a window on the screen.
- **on_yes()**: Function called when the user selects "Yes". Opens a confirmation window and executes the command if the phrase is correct.
- **on_no()**: Function called when the user selects "No". Closes the application.
- **root**: Main application window.

## Customization

You can customize the reminder message and confirmation phrase by editing the `settings.json` file. Additionally, you can change the path to the executable and other parameters necessary for executing the command.

## Contributions

Contributions are welcome! Feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
