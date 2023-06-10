import ecdsa
import os

# Gera uma chave privada aleatória
private_key = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1)

# Obtém a chave pública correspondente à chave privada gerada
public_key = private_key.get_verifying_key()

# Codifica as chaves em formato hexadecimal
private_key_hex = private_key.to_string().hex()
public_key_hex = public_key.to_string().hex()

# Deriva o endereço da carteira a partir da chave pública
ripemd160 = ecdsa.util.ripemd160(public_key.to_string())
address = ripemd160.hex()

print("Chave Privada: ", private_key_hex)
print("Chave Pública: ", public_key_hex)
print("Endereço da Carteira: ", address)
