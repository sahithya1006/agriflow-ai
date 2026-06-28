import sqlite3
from pathlib import Path

DB_PATH = Path("agriflow.db")


def get_connection():
    return sqlite3.connect(DB_PATH)


def init_db():
    conn = get_connection()
    cur = conn.cursor()
    cur.executescript("""
        CREATE TABLE IF NOT EXISTS farmers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            village TEXT,
            crop TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );

        CREATE TABLE IF NOT EXISTS predictions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            input_type TEXT,
            crop TEXT,
            disease TEXT,
            severity TEXT,
            recommendation TEXT,
            confidence REAL,
            raw_json TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );

        CREATE TABLE IF NOT EXISTS reports (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            prediction_id INTEGER,
            report_type TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );

        CREATE TABLE IF NOT EXISTS history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            action TEXT,
            details TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """)
    conn.commit()
    conn.close()


def save_prediction(
    input_type, crop, disease, severity, recommendation, confidence, raw_json
):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        """
        INSERT INTO predictions
        (input_type, crop, disease, severity, recommendation, confidence, raw_json)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """,
        (input_type, crop, disease, severity, recommendation, confidence, raw_json),
    )
    conn.commit()
    conn.close()


def get_all_predictions():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM predictions ORDER BY created_at DESC")
    rows = cur.fetchall()
    conn.close()
    return rows
