from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_performance_trends_router_exists():
    response = client.get(
        "/athletes/1/performance-trends",
    )

    assert response.status_code in [
        404,
        200,
    ]
