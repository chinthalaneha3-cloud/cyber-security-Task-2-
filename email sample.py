print("PHISHING EMAIL ANALYZER")

sender = input("Enter sender email: ")
message = input("Enter email message: ")

print("\n--- Report ---")

if "@" not in sender:
    print("Invalid email")
else:
    print("Sender email checked")

if "urgent" in message.lower():
    print("Warning: Urgent words found")

if "click" in message.lower():
    print("Warning: Suspicious link/message")

if "password" in message.lower():
    print("Warning: Password request found")

print("\nAnalysis completed.")