import requests
import sys
import json
from PyQt5.QtWidgets import QApplication, QDialog, QListView
from PyQt5.QtCore import QStringListModel, QModelIndex
from PyQt5.uic import loadUi
from datetime import datetime
from dotenv import dotenv_values
from ui_main import Ui_userInterface
from pprint import pprint

env_vars = dotenv_values('.env')

BASE_URL = "https://api.openai.com/v1/models"
API_KEY = env_vars['OpenAIKey']

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_KEY}"
}

def list_models():
    response = requests.get(BASE_URL, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Failed to get models: {}".format(response.status_code))

def get_model_details(model_id):
    response = requests.get(f"{BASE_URL}/{model_id}", headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Failed to get model details: {}".format(response.status_code))

def display_model_details(index):
    selected_index = index.row()
    selected_model = sorted_models[selected_index]
    model_id = selected_model['id']
    model_details = get_model_details(model_id)

    created_timestamp = int(model_details['created'])
    created_date = datetime.fromtimestamp(created_timestamp).strftime('%Y-%m-%d %H:%M:%S')
    model_info = f"Model: {model_details['id']}\n" \
                 f"Created: {created_date}\n" \
                 f"Owned By: {model_details['owned_by']}\n" \
                 f"Root: {model_details['root']}\n" \
                 f"Parent: {model_details['parent']}\n" \
                 f"\nPermissions:\n"

    permissions = model_details.get('permission', [])
    if permissions:
        for permission in permissions:
            model_info += f"ID: {permission['id']}\n" \
                          f"Created: {permission['created']}\n" \
                          f"Allow Create Engine: {permission.get('allow_create_engine', False)}\n" \
                          f"Allow Sampling: {permission.get('allow_sampling', False)}\n" \
                          f"Allow Logprobs: {permission.get('allow_logprobs', False)}\n" \
                          f"Allow Search Indices: {permission.get('allow_search_indices', False)}\n" \
                          f"Allow View: {permission.get('allow_view', False)}\n" \
                          f"Allow Fine Tuning: {permission.get('allow_fine_tuning', False)}\n" \
                          f"Organization: {permission.get('organization', '')}\n" \
                          f"Group: {permission.get('group', '')}\n" \
                          f"Is Blocking: {permission.get('is_blocking', False)}\n" \
                          f"\n"
    else:
        model_info += "No permissions found.\n"

    model_details_text.setText(model_info)

if __name__ == "__main__":
    app = QApplication([])
    dialog = QDialog()
    ui = Ui_userInterface()
    ui.setupUi(dialog)

    model_list_widget = ui.modelsList
    model_details_text = ui.modelDetails

    model_exit_button = ui.modelExit
    model_exit_button.clicked.connect(dialog.accept)

    models = list_models()
    sorted_models = sorted(models['data'], key=lambda x: x['created'])
    model_names = [model['id'] for model in sorted_models]

    model_list_model = QStringListModel(model_names)
    model_list_widget.setModel(model_list_model)

    model_list_widget.clicked.connect(display_model_details)

    model_details_text.setReadOnly(True)

    dialog.show()
    sys.exit(app.exec_())
