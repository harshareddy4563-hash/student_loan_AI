CREATE TABLE IF NOT EXISTS loans (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_name TEXT,
    parent_name TEXT,
    loan_amount INTEGER,
    status TEXT,
    kyc_score REAL
);
