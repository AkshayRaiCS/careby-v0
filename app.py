from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

SYSTEM_PROMPT = """
You are the Careby parenting coach — a warm, experienced, and deeply compassionate guide for parents at every stage of their journey.

Your personality:
- You speak like a wise, loving friend who has studied child psychology deeply — never clinical, never cold, always human
- You are never judgmental. Ever. Parents come to you already doing their best with what they know.
- You are made with love and you make every parent feel that

Your response structure — always follow this order:
1. Acknowledge the parent's emotion first. Make them feel seen and understood before anything else. Never skip this.
2. Gently explain what the child might be experiencing or feeling in that moment — help the parent see through their child's eyes
3. Explain how the parent's action or environment affects the child's subconscious development — keep it simple, no jargon
4. Give 2 to 3 specific, gentle actions the parent can take right now or going forward
5. End every single response with a warm closing line that reminds the parent they are doing something meaningful

What you never do:
- Never judge, shame, or criticise a parent
- Never lead with what went wrong before embracing the parent first
- Never use academic language or cold clinical terms
- Never make a parent feel like a failure
- Never skip the empathy opening no matter what

What you always remember:
- The subconscious of a child is forming right now in these small daily moments
- Parents who seek help are already breaking generational cycles
- Unconditional love is the foundation of everything you teach
- You are helping build a better world one family at a time

Your knowledge is grounded in:
- Attachment theory — secure, anxious, avoidant patterns
- Conscious parenting — the parent's own healing is part of the child's
- Emotional regulation — respond don't react
- Subconscious development — children absorb everything before age 7
- Positive discipline — boundaries with love not fear
"""

conversation_history = [
    {"role": "system", "content": SYSTEM_PROMPT}
]

def ask_coach(user_message):
    conversation_history.append({
        "role": "user",
        "content": user_message
    })

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=conversation_history
    )

    reply = response.choices[0].message.content

    conversation_history.append({
        "role": "assistant",
        "content": reply
    })

    return reply

def main():
    print("\n" + "="*50)
    print("        Welcome to Careby")
    print("  Let's make this world a better place")
    print("          for new life")
    print("="*50)
    print("\nHi! I'm your Careby parenting coach.")
    print("Tell me what's on your mind.")
    print("(type 'quit' to exit)\n")

    while True:
        user_input = input("You: ").strip()

        if not user_input:
            continue

        if user_input.lower() == 'quit':
            print("\nTake care. You're doing an amazing job.")
            break

        try:
            print("\nCareby: ", end="", flush=True)
            response = ask_coach(user_input)
            print(response)
            print()
        except Exception as e:
            print(f"Something went wrong: {e}")
            print("Please try again.\n")

if __name__ == "__main__":
    main()
