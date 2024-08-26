---

# **Gemini Explorer**

## **Overview**

Gemini Flight Manager is a backend system developed using FastAPI, designed to manage and simulate flight-related operations. It offers a high-performance platform for handling various aspects of flight management, such as flight generation, search, and booking functionalities.

The system leverages FastAPI's efficient framework to create a scalable solution for managing flight data. It comes with an SQLite database (`flights.db`) pre-populated with initial data, allowing for easy deployment and testing.

### **Key Features**:
- **Advanced Flight Search**: Query flights based on criteria like origin, destination, and dates.
- **Booking System**: Manage seat availability across different classes, calculating costs accordingly.
  
Gemini Flight Manager is built for extensibility and scalability, making it ideal for both educational purposes and as a foundation for more complex flight management systems.

**Note**: For the Gemini Function Calling project, only the `search_flights` and `book_flight` functions are needed.

---

## **Installation**

### **Prerequisites**
Before you begin, ensure you have the following installed:
- Python 3.6 or higher
- FastAPI
- Uvicorn (ASGI server for FastAPI)

### **Step-by-Step Installation Guide**

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/your-repository.git
   cd your-repository
   ```

2. **Set Up a Virtual Environment (Optional but Recommended)**
   Create a virtual environment to isolate dependencies:
   ```bash
   virtualenv venv
   source venv/bin/activate
   ```

3. **Install Dependencies**
   Inside the virtual environment, install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. **Start the FastAPI Server**
   Start the FastAPI server using Uvicorn:
   ```bash
   uvicorn main:app --reload
   ```

5. **Accessing the API**
   Once the server is running, access the API at `http://127.0.0.1:8000`. For interactive documentation, visit `http://127.0.0.1:8000/docs`.

---

## **Mission Scenario**

Create a user-friendly chat interface using Streamlit that connects with Google's state-of-the-art large language model, Gemini. This project aims to serve as an educational and practical introduction to integrating large language models with intuitive interfaces.

---

### **Mission Workflow**

- **Task 1: 🌐 Enable Google Cloud**
  - Sign up or sign in to [Google Cloud](https://cloud.google.com).
  - Set up billing if necessary and enable essential APIs, such as the AI Platform API and Google Gemini API.

- **Task 2: 🧬 Google Cloud Initialization**
  - Create a new project within the Google Cloud Console.
  - Set up the necessary service accounts and assign roles (e.g., AI Platform Admin, Google Gemini User).
  - Generate and securely store the JSON key file for authentication.

- **Task 3: ☁️ Setting up Google Gemini**
  - Install Streamlit:
    ```bash
    pip install streamlit
    ```
  - Integrate Google Gemini to leverage its AI-driven content analysis.
  - Ensure the correct APIs are enabled, and your service account has the required permissions.

- **Task 4: 📊 Streamlit Integration**
  - Implement a user-friendly interface with Streamlit, allowing users to upload documents, interact with quizzes, and receive feedback.
  - Run the app:
    ```bash
    streamlit run filename.py
    ```

- **Task 5: 🗣️ Adding Initial System Messages**
  - Add system messages to guide users through the process, enhancing the overall user experience.

- **Task 6: 📄 Preparing Submission**
  - Prepare a GitHub repository with all project files, including a README, code files, and documentation.
