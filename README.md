# Image_To_Text_Converter
This a Image to text converter tool using COHERE API and Hugging Face API.


This tool takes an image as an input and generates a scenario which is nothing but a small description of the image that is generated. Further more the tool generates a random story based on the small description that is generated early than this. The story generated is related to the generated scenario which is very random.

![download](https://github.com/user-attachments/assets/a2121691-7151-4baa-bdc1-62cd7e5e7287)

To use the project from GitHub, anyone can follow these steps:

 #### Step 1: Clone the Repository
To clone the project from GitHub to a local machine, use the following command:

1. **Copy the repository URL**:
   - Go to your GitHub repository page.
   - Click the green "Code" button.
   - Copy the URL (HTTPS or SSH).

2. **Open a terminal on your machine and run**:
   ```bash
   git clone https://github.com/YourUsername/YourRepoName.git
   ```
   Replace `YourUsername/YourRepoName` with the actual username and repository name.

3. **Navigate to the cloned repository**:
   ```bash
   cd YourRepoName
   ```

 ### Step 2: Set Up the Project Locally
Once the code is cloned, follow these steps to run it on a local machine.

 #### Option 1: Using Python's Built-In Environment Management
1. **Create a virtual environment**:
   ```bash
   python -m venv venv
   ```

2. **Activate the virtual environment**:
   - On Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

3. Install dependencies:
   The repository should contain a `requirements.txt` file, which lists all the dependencies.
   ```bash
   pip install -r requirements.txt
   ```

#### Option 2: Using `pipenv` (Alternative)
If you're using `pipenv`, you can install dependencies and create a virtual environment with:
```bash
pipenv install
pipenv shell
```

### Step 3: Add API Keys to `.env` File
Make sure to provide the necessary API keys (Cohere, Hugging Face, etc.):

1. Create a `.env` file in the root directory of the project if it doesn’t already exist.
2. Add the following content to your `.env` file:
   ```bash
   HUGGINGFACE_API_TOKEN=your_huggingface_api_key
   COHERE_API_KEY=your_cohere_api_key
   ```

### Step 4: Run the Application
You can now run the Streamlit app:

```bash
streamlit run app.py
```

This will start the Streamlit server, and the app will open in the default web browser.

### Step 5: Access the Application in a Browser
Once Streamlit starts running, it will provide a local URL, usually something like:
```
http://localhost:8501
```
Open that link in a web browser to use the application.

### Summary of Steps:
1. **Clone the repository**: `git clone <repo-url>`
2. **Navigate to the project directory**: `cd YourRepoName`
3. **Create and activate a virtual environment**:
   - Windows: `.\venv\Scripts\activate`
   - macOS/Linux: `source venv/bin/activate`
4. **Install dependencies**: `pip install -r requirements.txt`
5. **Add API keys** to the `.env` file.
6. **Run the Streamlit app**: `streamlit run app.py`

Once these steps are completed, the application should be running and available for use.


