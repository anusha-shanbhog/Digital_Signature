import sys
import os
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
from Crypto.Signature import PKCS1_v1_5
from pyfiglet import Figlet

    
def generate_key_pair():
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    
    with open("private_key.pem", "wb") as f:
        f.write(private_key)

    with open("public_key.pem", "wb") as f:
        f.write(public_key)


def sign_document(document_path):
    private_key_path = "private_key.pem"
    signature_path = "signature.bin"

    if not (os.path.isfile(private_key_path) and os.path.isfile(signature_path)):
        print("Private key or signature file missing. Generating key pair and signature file...")
        generate_key_pair()

    with open(private_key_path, "rb") as f:
        private_key = RSA.import_key(f.read())

    with open(document_path, "rb") as f:
        document_data = f.read()

    document_hash = SHA256.new(document_data)

    signer = PKCS1_v1_5.new(private_key)
    signature = signer.sign(document_hash)

    with open(signature_path, "wb") as f:
        f.write(signature)

    print("Document signed successfully. Signature saved to", signature_path)


def verify_signature(document_path, public_key_path, signature_path):
    if not (os.path.isfile(public_key_path) and os.path.isfile(signature_path)):
        print("Public key or signature file missing.")
        return

    with open(public_key_path, "rb") as f:
        public_key = RSA.import_key(f.read())

    with open(document_path, "rb") as f:
        document_data = f.read()

    document_hash = SHA256.new(document_data)

    with open(signature_path, "rb") as f:
        signature = f.read()

    verifier = PKCS1_v1_5.new(public_key)
    if verifier.verify(document_hash, signature):
        print("Signature is valid.")
    else:
        print("Signature is not valid.")
 


def main():
    
    if len(sys.argv) < 3:
        print("Usage: python digital_signature_tool.py <-s|-v> <document> [public_key] [signature]")
        return

    option = sys.argv[1]
    document_path = sys.argv[2]

    if option == "-s":
        sign_document(document_path)
    elif option == "-v":
        if len(sys.argv) != 5:
            print("Usage: python digital_signature_tool.py -v <document> <public_key> <signature>")
            return
        public_key_path = sys.argv[3]
        signature_path = sys.argv[4]
        verify_signature(document_path, public_key_path, signature_path)
    else:
        print("Invalid option. Usage: python digital_signature_tool.py <-s|-v> <document> [public_key] [signature]")


if __name__ == "__main__":
    main()

    # Add your existing tool code here


