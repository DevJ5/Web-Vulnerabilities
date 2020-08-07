# Attacks

TLS 1.2 uses more roundtrips and sends the encrypted symmetric key over the wire.
TLS 1.3 uses diffie helmann and only sends a root prime, modulus and a calculation over the wire. The other party has then enough to calculate the symmetric key.

TLS does this handshake before establishing a secure connection which is called https.

Certificates are files with data. They contain a hashing algorithm because the certificate is too large to sign, so we hash first and then sign using a private key. In the certificate is the public key. Serial number is a unique number for this certificate.
