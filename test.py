import jwt
import datetime



def generate_jwt(user_id):
    try:
        payload = {
            'exp': datetime.datetime() + datetime.timedelta(days=0, minutes=60),
            'iat': datetime.datetime(),
            'sub': user_id
        }
        return jwt.encode(
            payload,
            key='12345',
            algorithm='HS256'
        )
    except Exception as e:
        return e


token = generate_jwt('12345')


token = str.encode('eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1NzQ4ODgyMDAsImlhdCI6MTU3NDg4ODE5NSwic3ViIjoiMTIzNDUifQ.')




def decode_auth_token(auth_token):

    try:
        payload = jwt.decode(auth_token, 'test', verify=False)
        return payload['sub']
    except jwt.ExpiredSignatureError:
        return '401 Error: Signature expired'
    except jwt.InvalidTokenError:
        return '401 Error:Invalid token'

print(decode_auth_token(token))

