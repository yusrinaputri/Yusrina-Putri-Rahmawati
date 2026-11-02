def send_messages(messages, sent_messages):
    """Menampilkan tiap pesan dan memindahkannya ke sent_messages."""
    while messages:
        current_message = messages.pop()
        print(f"Mengirim pesan: {current_message}")
        sent_messages.append(current_message)


texts = ['Halo!', 'Lagi apa?', 'Nanti malam jadi belajar bareng ya.']
sent_messages = []

send_messages(texts, sent_messages)

print(texts)
print(sent_messages)