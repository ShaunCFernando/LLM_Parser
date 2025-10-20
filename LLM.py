import ollama
import os

def askLLM(report_content):
    response = ollama.chat(model = 'llama3', messages = 
    [
        {
            'role': 'user',
            'content': f'Identify/Find/Determine if the patient in this report does not present chest pains: \n\n {report_content}',
        },
    ],

    options = 
    {
        'temperature': 0.7,
        'seed': 42
    })
    return response['message']['content']

def check_discharge_reports(path):
    results = {}
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        if os.path.isfile(file_path) and file_path.endswith('.txt'):
            with open(file_path, 'r') as file:
                report_content = file.read()
                response = askLLM(report_content)
                results[file_path] = response
    return results

folder_path = '/Users/sfern4850/Documents/Hillman_Academy_2024/PythonAutomation/upmc_clinical_er_discharge'

results = check_discharge_reports(folder_path)
for report, result in results.items():
    print(f'Report: {report}\nResult: {result}\n')
