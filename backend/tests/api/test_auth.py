def test_register_user(client):
    response = client.post(
        "/auth/register",
        json={
            "email": "test@example.com",
            "full_name": "Test User",
            "password": "Password123",
        },
    )

    assert response.status_code == 201

    data = response.json()

    assert data["email"] == "test@example.com"
    assert data["full_name"] == "Test User"


def test_register_duplicate_email(client):
    # Register the user the first time
    client.post(
        "/auth/register",
        json={
            "email": "duplicate@example.com",
            "full_name": "Duplicate User",
            "password": "Password123",
        },
    )

    # Try to register the same email again
    response = client.post(
        "/auth/register",
        json={
            "email": "duplicate@example.com",
            "full_name": "Duplicate User",
            "password": "Password123",
        },
    )

    assert response.status_code == 400

    data = response.json()

    assert data["detail"] == "Email is already registered."


def test_login_success(client):
    # Register a user
    client.post(
        "/auth/register",
        json={
            "email": "login@example.com",
            "full_name": "Login User",
            "password": "Password123",
        },
    )

    # Log in
    response = client.post(
        "/auth/login",
        data={
            "username": "login@example.com",
            "password": "Password123",
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert "access_token" in data
    assert data["token_type"] == "bearer"


def test_login_invalid_password(client):
    # Register a user
    client.post(
        "/auth/register",
        json={
            "email": "invalid@example.com",
            "full_name": "Invalid Password User",
            "password": "Password123",
        },
    )

    # Attempt login with the wrong password
    response = client.post(
        "/auth/login",
        data={
            "username": "invalid@example.com",
            "password": "WrongPassword123",
        },
    )

    assert response.status_code == 401

    data = response.json()

    assert data["detail"] == "Invalid email or password."


def test_login_unknown_email(client):
    response = client.post(
        "/auth/login",
        data={
            "username": "unknown@example.com",
            "password": "Password123",
        },
    )

    assert response.status_code == 401

    data = response.json()

    assert data["detail"] == "Invalid email or password."


def test_get_current_user(client):
    # Register a user
    client.post(
        "/auth/register",
        json={
            "email": "me@example.com",
            "full_name": "Current User",
            "password": "Password123",
        },
    )

    # Login
    login_response = client.post(
        "/auth/login",
        data={
            "username": "me@example.com",
            "password": "Password123",
        },
    )

    assert login_response.status_code == 200

    token = login_response.json()["access_token"]

    # Access the protected endpoint
    response = client.get(
        "/auth/me",
        headers={
            "Authorization": f"Bearer {token}",
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["email"] == "me@example.com"
    assert data["full_name"] == "Current User"


def test_get_current_user_without_token(client):
    response = client.get("/auth/me")

    assert response.status_code == 401

    data = response.json()

    assert data["detail"] == "Not authenticated"


def test_get_current_user_invalid_token(client):
    response = client.get(
        "/auth/me",
        headers={
            "Authorization": "Bearer invalid-token",
        },
    )

    assert response.status_code == 401

    data = response.json()

    assert data["detail"] == "Invalid or expired token."
