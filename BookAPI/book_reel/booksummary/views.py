from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from groq import Groq
import os
# Create your views here.


def index(response):
    return render(response,'index.html')


@login_required
def profile(request):
    book_summary = ""
    api_key = os.environ.get("GROQ_API_KEY")

    if not api_key:
        raise ValueError("GROQ_API_KEY environment variable not set")
    
    print("GROQ_API_KEY:", api_key)
    if request.method == "POST":
        book_name = request.POST.get("book_name")
        client = Groq(api_key=api_key)

        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": "Give the summary of " + book_name + " book",
                }
            ],
            model="llama3-8b-8192",
        )

        book_summary = chat_completion.choices[0].message.content

    return render(request, 'profile.html', {"book_summary": f"{book_summary}"})