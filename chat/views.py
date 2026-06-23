from django.shortcuts import render
from django.http import JsonResponse
from .models import ChatMessage
import ollama

def chat_page(request):
    return render(request, "chat/chat.html")

def chat_response(request):
    print("🔥 CHAT_RESPONSE HIT 🔥")

    if request.method == "POST":
        user_msg = request.POST.get("message")

        try:
            response = ollama.chat(
                model="llama3",
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "You are Senthur Poultry AI assistant. "
                            "Answer politely about poultry farming, "
                            "prices, locations, and services. "
                            "Keep responses short and simple."
                        )
                    },
                    {
                        "role": "user",
                        "content": user_msg
                    }
                ]
            )

            reply = response["message"]["content"]

        except Exception as e:
            print("OLLAMA ERROR:", e)
            reply = "⚠️ Local AI not responding."

        ChatMessage.objects.create(
            user_message=user_msg,
            bot_reply=reply
        )

        return JsonResponse({"reply": reply})
