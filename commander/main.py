from .sender import encrypted_send_payload
import base64


def main():
    """
    Main function for commander
    """
    payload = b"print('Hello World!')"
    output = encrypted_send_payload(payload)
    print(output) # Should print Hello World!
