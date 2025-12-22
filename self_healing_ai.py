import google.generativeai as genai
import sys
import time

# --- STEP 1: AI CONFIGURATION ---
# Replace 'YOUR_API_KEY' with your actual key from Google AI Studio
genai.configure(api_key="YOUR_API_KEY")

# Using the 2025 flagship model for complex code reasoning
model = genai.GenerativeModel('gemini-1.5-pro')

def run_automated_process():
    """
    A function designed to fail to demonstrate 
    the AI's self-healing capabilities.
    """
    print("\n[SYSTEM] Starting automated data process...")
    time.sleep(1)
    
    try:
        # LOGICAL ERROR: Attempting to perform math on incompatible types
        raw_data = "100"
        divisor = 0
        print(f"[LOG] Attempting calculation: {raw_data} / {divisor}")
        
        result = int(raw_data) / divisor
        return result

    except Exception as e:
        handle_system_error(e)

def handle_system_error(error):
    """
    Captures the stack trace and consults Gemini AI for a fix.
    """
    print(f"\n[!] CRITICAL ERROR DETECTED: {error}")
    print("[...] Consulting AI Healer for a patch...")
    
    # Constructing a high-context prompt for the AI
    prompt = (
        f"The following Python error occurred in my script: '{error}'. "
        "Please provide a brief explanation of why this happened and "
        "the corrected Python code to fix it."
    )
    
    try:
        response = model.generate_content(prompt)
        print("\n--- AI HEALER RECOMMENDATION ---")
        print(response.text)
        print("---------------------------------")
    except Exception as ai_err:
        print(f"Failed to connect to AI Brain: {ai_err}")

# --- MAIN EXECUTION ---
if __name__ == "__main__":
    run_automated_process()
    print("\n[SYSTEM] Process finished. Check AI logs above.")
