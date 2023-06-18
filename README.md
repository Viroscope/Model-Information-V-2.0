# Model Information V 2.0

This code provides a graphical user interface for viewing details of OpenAI models using the OpenAI API. The interface is built using PyQt5.

## Prerequisites

Before running the code, make sure you have the following dependencies installed:

- `requests`
- `json`
- `PyQt5`
- `dotenv`
- `pprint`

Install these dependencies by running `pip install -r requirements.txt` in your terminal or command prompt.

## Configuration

Create a `.env` file in the same directory as the code and add your OpenAI API key as follows:

```
OpenAIKey=<your-api-key>
```

## Usage

Run the code by executing the Python script. The user interface will appear, showing a list of available models.

- Click on a model in the list to display its details on the right side.
- The model details include the model ID, creation date, owner, root, parent, and permissions.
- If permissions exist for the model, they will be displayed with additional information such as ID, creation date, and various access controls.

## Code Explanation

- The code starts by importing the necessary modules and libraries.
- It then loads the `.env` file to retrieve the OpenAI API key.
- The `list_models()` function sends a GET request to the OpenAI API to retrieve a list of available models.
- The `get_model_details()` function retrieves detailed information about a specific model using its ID.
- The `display_model_details()` function is called when a model is clicked in the list. It fetches the model details and formats them into a human-readable string, which is then displayed in the user interface.
- The main entry point of the code checks if it's being executed directly and not imported as a module. It creates the application and the dialog window for the user interface.
- The UI is set up using the `Ui_userInterface` class.
- The `modelsList` widget displays the list of model names.
- The `modelDetails` widget shows the details of the selected model.
- The `modelExit` button allows the user to close the application.
- The list of models is retrieved and sorted by creation date.
- The model names are extracted from the sorted models and added to the `model_list_model`, which is then set as the data source for the `model_list_widget`.
- When a model is clicked in the list, the `display_model_details()` function is called to update the `model_details_text` widget with the details of the selected model.
- Finally, the application is shown, and the event loop is started.

That's it! You can now view the details of OpenAI models using this simple graphical user interface.
