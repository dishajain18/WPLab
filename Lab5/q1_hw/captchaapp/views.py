from django.shortcuts import render
import random
import string

# Function to generate a random CAPTCHA
def generate_captcha():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

# Store the CAPTCHA value globally (Ideally, use sessions)
captcha_value = generate_captcha()
attempts = 0  # Track failed attempts

def captcha_view(request):
    global captcha_value, attempts

    message = ""
    disable_input = False

    if request.method == "POST":
        user_input = request.POST.get("captcha_input")
        
        if user_input == captcha_value:
            message = "✅ Correct! CAPTCHA matched."
            attempts = 0  # Reset on success
            captcha_value = generate_captcha()  # Generate a new CAPTCHA
        else:
            attempts += 1
            message = f"❌ Incorrect! Attempts: {attempts}"
            
            if attempts >= 3:
                disable_input = True
                message = "❌ Too many failed attempts. Input disabled."

    return render(request, "captcha.html", {
        "captcha_text": captcha_value,
        "message": message,
        "disable_input": disable_input
    })
