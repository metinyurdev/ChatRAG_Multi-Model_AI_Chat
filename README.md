# 🔎 Chat RAG - AI Chatbot with Multi-Model Support

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python) 
![Streamlit](https://img.shields.io/badge/Streamlit-1.0-red?style=for-the-badge&logo=streamlit) 
![LangChain](https://img.shields.io/badge/LangChain-%23FFD43B?style=for-the-badge&logo=langchain&logoColor=black)   
![Ollama](https://img.shields.io/badge/Ollama-AI-green?style=for-the-badge&logo=ollama) 

## 📌 Project Description
Chat RAG is a user-friendly, Retrieval-Augmented Generation (RAG)-powered AI chatbot. Users can select one of four different models via the toggle bar in the upper right corner and start chatting. Chat history is stored in `.json` format and can be accessed from the left side of the page.

### 🚀 Key Features
- 🌗 **Day & Night Mode**: Light mode during the day, automatically switches to dark mode at night.
- 🔄 **Clear History**: Reset chat history with the "Clear Chat History" button.
- 🇬🇧 **Multi-Language Support**: Responds in English by default, but can answer in Turkish upon request.
- 🛠️ **Modular Structure**: Supports four different language models.
- 💾 **Chat History Storage**: The last 8 messages are automatically saved in a `.json` file.

## 🎥 Project Demo Video
Watch the project demo video below:

! **Watch Video:** [Video](Project_Demo_Video.mp4)

! **Watch Video from DRIVE:** [Video_Drive](https://drive.google.com/drive/folders/1gc_4sFwvqIUtBIweVcc1092NjRsN2j2B)


## 🚀 Technologies Used

| Technology  | Description |
|------------|---------|
| ![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=flat&logo=python) | Main programming language |
| ![Streamlit](https://img.shields.io/badge/Streamlit-1.0-red?style=flat&logo=streamlit) | User-friendly UI framework |
| ![LangChain](https://img.shields.io/badge/LangChain-%23FFD43B?style=flat&logo=langchain&logoColor=black) | LLM integration |
| ![Ollama](https://img.shields.io/badge/Ollama-AI-green?style=flat&logo=ollama) | Running AI models |

## 📂 Project Structure
```
chat_rag/
│── mynewenv # Python virtual environment
│── app.py  # Main application file
│── history.json  # Stores the last 8 messages
│── Project_Demo_Video.mp4  # Demo video file
│── requirements.txt  # Dependencies
└── README.md  # Project documentation
```

## 📥 Installation & Usage

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/metinyurdev/ChatRAG_Multi-Model_AI_Chat
cd ChatRAG_Multi-Model_AI_Chat
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Application
```bash
streamlit run app.py
```

🔹 **That's it!** Access the chatbot at `http://localhost:8501` in your browser. 🚀

---
✍ **Developer:** [Metin YURDUSEVEN](https://github.com/metinyurdev)
