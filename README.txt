# Text-to-Image AI (Stable Diffusion with Diffusers)

## STEP 1: Install Python (if you haven't)
Go to https://www.python.org/downloads/ and install Python 3.10+
Be sure to check "Add Python to PATH"

## STEP 2: Open this project folder in VS Code

## STEP 3: (Optional but recommended)
Create a virtual environment:
  python -m venv venv

Activate it:
  venv\Scripts\activate  (Windows)
  source venv/bin/activate  (Mac/Linux)

## STEP 4: Install requirements
Run:
  pip install -r requirements.txt

## STEP 5: Set up Hugging Face token
1. Go to https://huggingface.co/
2. Create an account
3. Go to: https://huggingface.co/settings/tokens
4. Create a token with "Read" access
5. Run the script, and paste your token when asked

## STEP 6: Run the script
  python generate_image.py

Wait for model to download. Then the image will appear and be saved as 'output.png'.
