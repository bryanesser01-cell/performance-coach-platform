from app.security.jwt import create_access_token

token = create_access_token(
    {
        "sub": "bryan@example.com"
    }
)

print(token)