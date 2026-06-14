from memory.memory_manager import MemoryManager

memory = MemoryManager()

memory.save_conversation(
    "demo",
    [
        {
            "role": "user",
            "content": "Hola TripleA",
        },
        {
            "role": "assistant",
            "content": "Hola, ¿cómo puedo ayudarte?",
        },
    ],
)

conversation = memory.load_conversation("demo")

print(conversation)