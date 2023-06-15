# RSA-encryption
Program for RSA encryption

RSA encryption is asymmetric: it uses a pair of keys (whole numbers) consisting of a public key to encrypt and a private key to decrypt confidential data. Both keys are created by a person, often conventionally named Alice, who wants confidential data sent to her. Alice makes the public key accessible. This key is used by its correspondents (Bob, etc.) to encrypt the data sent to it. The private key is reserved for Alice, and allows her to decrypt this data. The private key can also be used by Alice to sign data that she sends, the public key allowing any of her correspondents to verify the signature.

An essential condition is that it be "computationally impossible" to decipher using only the public key, in particular to reconstitute the private key from the public key, that is to say that the means of calculation available and the methods known at the time of the exchange (and the time that the secrecy must be kept) do not allow it.

RSA encryption is often used to communicate a symmetric encryption key, which then allows the exchange to continue confidentially: Bob sends Alice a symmetric encryption key which can then be used by Alice and Bob to exchange data.
