import google.generativeai as genai

genai.configure(api_key="AIzaSyAl5ECilHNMGgma5RFbsB7sZp00Ku3aS_E")

for m in genai.list_models():
    print(m.name)
