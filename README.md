This Python tool ensures the integrity and authenticity of your documents using digital signatures.
It generates a private-public RSA key pair, with the private key used for signing and the public key for verification. 
SHA-256 is used to hash the document to create a unique fingerprint, integral to the digital signature process. It signs documents by encrypting the SHA-256 hash with the private key. 
To verify, it decrypts the signature using the provided public key and checks for a match with the document's hash. A match validates the signature's authenticity.


Steps to run: 


1. python digital_signature.py -s `<document>`

   
This command generates an RSA key pair, if it doesn't exist, and signs the specified document. The digital signature is saved in a file named "signature.bin." The private key is stored in "private_key.pem," and the public key is stored in "public_key.pem."
  
2. python digital_signature.py -v `<document>` `<public_key>` `<signature>`


Verify the authenticity of a document by providing the document, the public key, and the corresponding signature. The tool checks whether the document's signature is valid, ensuring it hasn't been tampered with.



Screenshot of working of tool:

/home/anu/digver.png



   

