import sqlite3
from database.db import init_db, get_connection, save_prediction, get_all_predictions


def test_tables_exist():
    init_db()
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = [r[0] for r in cur.fetchall()]
    conn.close()
    assert "farmers" in tables
    assert "predictions" in tables
    assert "reports" in tables
    assert "history" in tables


def test_connection_returns_sqlite():
    conn = get_connection()
    assert isinstance(conn, sqlite3.Connection)
    conn.close()


def test_save_and_retrieve_prediction():
    init_db()
    save_prediction(
        input_type="text",
        crop="Tomato",
        disease="Early Blight",
        severity="High",
        recommendation="Apply fungicide",
        confidence=0.92,
        raw_json='{"test": true}',
    )
    rows = get_all_predictions()
    assert len(rows) >= 1
    assert rows[0][3] == "Early Blight"  # disease column
