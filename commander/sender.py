from .settings import PORTS, COMMAND_PORT, IP, RSA_KEY
from general.enc_layer import encrypt_data, decrypt_and_validate_data

def encrypted_send_payload(data: bytes)-> bytes:
    """
        This function performs the port knocking, it then connects to the COMMAND_PORT and sends the encrypted payload.
        The response is then decrypted and returned.
    """
    pass