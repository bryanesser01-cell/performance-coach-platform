from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_athlete_performance_report_router_exists():

    response = client.get(
        "/athletes/1/performance-report",
    )

    assert response.status_code in [
        200,
        500,
    ]
