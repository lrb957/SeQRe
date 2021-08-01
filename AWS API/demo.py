import base64
from Crypto.Random import get_random_bytes
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Hash import SHA256


private_key = b'MIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQC8nRTnRduk1ADfsqUVVW8J5yQ8P7UF4DKv/B+p867wrfyIcZAR6eMb0PWh7SermSeNnJArAL279PnkQEaQswv7sJ/ecAJMrB50ouojHNwS0vKetcXjbEhgR39TBjcOZePIa/PhJu3e+mi+3EzVZ9RqAJmMC951r9k49m3PTyXjrQ9Hpg4WzJenxtdYhEfs9Av/XOkzR2IaT1JGpuaLGn1hjv9ZzW6Qb0KoRle6ibhhD88cr+IAKRVq0YgXYZyIfzIsPRse4tAMz3ax/EQq02agKCmdTujlYZ0/evJZip0HdncqF/AtzV1Ji1WI/un8Z05onkpAWfqjyxg81L9e9itBAgMBAAECggEAXXiDCXHnPbIKlNFVWlMyaffwTyNLNJQ8ylXp4zFuOrwecAfHW/lKoVhWwl5i0HlfzqAOGiGN5X2r8V+hGMiCYcLQF03u9cw+c5Lg8XG15mY/8kMmxGO/ImeMQ7rKwgngbkyBWc0PCPeTvTIzqXaBH98YOP0Qy8XPopkNJjWVE1SvqjpI3DisjSLoJcaJdqHWB7J06GebeXTr/7sTaKfKUkcu4zxmIiBETnxemtrn/EY9TkFjztDyaHaQOurUq6V8PO0G0l07IV3UXMgA0eFw1Q1Pm0EkkVj2+py5WFLPuJHt/KSeWNVnkmetBjZZn6I+gwSSmkiWnDOQjGs7QkjogQKBgQDveXeZp+O8m/ZUIDFiGM8zdhT3jy7eesPuJZKTy309/TZW/3G62FB7IU9ujogqpJk97/iaX8qDsiqKlXCP5VPA/gAVZSKdN4ua2Wm6eXk7sAb5rZQ6uulIrd4MDK+m7+6UqLuVckoVP4O8+EouQsLtLeEKcnKeDxNCROEhh93vuQKBgQDJoRxxcyNeEQltmfrHtZD4Lefy8VJzIAm3bH0FrYnlmMRqKJxrm7GTPwKJVGoU4EdC1j34qQy52L2/rujOyhdPzcv+JczkmtWOfBRAX3ghZYbhA8qiq3F4X5QihzbeOrRF9Ypc/bnKuoDsl0zs3QDCO/3rFDxTShZmt+8ED6gLyQKBgAno5OIe6HWtnovsqR5+GFTw1f1Il4/tVJ5OP7qN+SjPiagf+fzZZrsxra/NhiT9mrnNbGQ3ApJglRIXDQlnXAfoeuhnvv7yhXxq8s0cqb+mkSNT44Zqpay0RTQKclpeI2lTci/FAvvOHQ182NUBPj/CXkWoZsXTqeBcKVTR4oVBAoGBAIgEsr5p8Nr9XUHd1UqyVqjFtyqx13AolcVyX2jcKCGGDEKdQOBq+MEfiaOBGcsZfZk+FDJSQG6DI4ZTBWSy+kTwzQOXFoDFXvmvBK5keRL2faYAO8u/Il4VBEbCtqX2LjTfrsaKt7JmXKC+dLt5X5CojePvE78QRMponMo9kZzZAoGBAN0M47HBV0IaADwnD8X9PRZZXAI9yhmaU2bCmXCo8xMTel705v+yp4AGPUMLuShEv2r8CMwj1IZABjEs8Utv06dbQ3HHqUSqa/akbGFTc9luRjv69QbywGXgA7Y9SKKYmIx85xGNQmTby7n60apphRm0JQwi6LGLS7CvBxGFukBJ'
private_key = base64.b64decode(private_key)
private_key = RSA.import_key(private_key)

c_auth = "ZAXlsTgdoyGbNqibzL4w9pnIBmuYDe4gPKAzL/ic4QkdnYhq5ESdpeXlZ5rOrrign9mMmkQv5AiYFX1uvy3iJKGGwpKOB9Nnhu4i9m0z1ESTUAQlJ623oys0v/WGzA4xS6jihwFY+k26GMUcgdePZHqIL42Ox8FHgux+UhDjjv3NhMLWKcGKNZrrsNBs7Wehe4C8RsdBHICu6DVyD9ogpuuQw98rK9oNMlE4aTNTZwUoYD02Ip3NHdPScMwZcuQpQoak3G0AcrRgWOg5S9xMsRQ03+59S2DYP2x1mXWLSRb9zuBNecmCUtbZ/edi3Q5okL7aRoUCVSyK88lWCYGsBg=="
base64_bytes = c_auth.encode('ascii')
message_bytes = base64.b64decode(base64_bytes)

cipher_rsa = PKCS1_OAEP.new(private_key)
decrypted = cipher_rsa.decrypt(message_bytes)
session_key = base64.b64encode(decrypted[:-1]).decode('ascii')
length = decrypted[-1]

sha256 = base64.b64encode(SHA256.new(decrypted[:-1]).digest()).decode('ascii')
otp = sha256[:length]

print('session key:', session_key)
print('length:', length)
print('otp:', otp)