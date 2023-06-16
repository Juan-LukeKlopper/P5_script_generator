# P5_script_generator

The project is a Streamlit application that takes an input, uses Langchain and OpenAI to chain prompts together, and generates a script that draws the input using P5.js.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## Installation

1. Clone the repository:

```bash
   git clone https://github.com/Juan-LukeKlopper/P5_script_generator.git
```
  
2. Navigate to the project directory:

```bash
cd P5_script_generator
```

3. Create a virtual environment:

```bash
python -m venv env
```

4. Activate the virtual environment:

For Windows:

```bash
env\Scripts\activate
```

For Unix or Linux:

```bash
source env/bin/activate
```

5. Install the dependencies:

```bash
pip install -r requirements.txt
```

6. Create apikey.py file in the project directory.

7. Open apikey.py and add the following code, replacing YOUR_API_KEY with your actual OpenAI API key:

```python
# apikey.py

apikey = 'YOUR_API_KEY'
```

8. Save the apikey.py file.

# Usage:

```bash
streamlit run app.py
```

# License:

This project is licensed under the MIT License. See the LICENSE file for details.
