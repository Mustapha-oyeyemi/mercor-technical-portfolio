import pandas as pd
import re
from datetime import datetime
from pathlib import Path


def audit_serial_inventory(file_path: str, output_report: str = "audit_exceptions.xlsx") -> dict:
    """
    Audits a hardware/terminal inventory spreadsheet for:
    1. Missing or null serial numbers
    2. Duplicate serial entries
    3. Non-compliant serial number formats (expected: 3 uppercase letters + 8 digits, e.g., TRM84920145)
    4. Active terminals missing assigned location IDs
    """
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"Input file not found: {file_path}")

    df = pd.read_excel(path) if path.suffix in [".xlsx", ".xls"] else pd.read_csv(path)

    # Normalize column names
    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

    required_cols = {"serial_number", "terminal_model", "status", "location_id"}
    missing_cols = required_cols - set(df.columns)
    if missing_cols:
        raise ValueError(f"Missing required columns in dataset: {missing_cols}")

    exceptions = []

    # 1. Check for null/blank serial numbers
    null_serials = df[df["serial_number"].isna() | (df["serial_number"].astype(str).str.strip() == "")]
    for idx, row in null_serials.iterrows():
        exceptions.append({
            "row_number": idx + 2,
            "serial_number": "MISSING",
            "issue_type": "Missing Serial Number",
            "details": f"Model '{row.get('terminal_model', 'Unknown')}' has no serial recorded."
        })

    # Clean valid strings for remaining checks
    valid_df = df.dropna(subset=["serial_number"]).copy()
    valid_df["serial_clean"] = valid_df["serial_number"].astype(str).str.strip().str.upper()

    # 2. Check for duplicate serial numbers
    duplicates = valid_df[valid_df.duplicated(subset=["serial_clean"], keep=False)]
    for idx, row in duplicates.iterrows():
        exceptions.append({
            "row_number": idx + 2,
            "serial_number": row["serial_clean"],
            "issue_type": "Duplicate Serial Number",
            "details": "Serial number appears multiple times in the inventory log."
        })

    # 3. Validate serial format (3 uppercase letters followed by 8 digits)
    serial_pattern = re.compile(r"^[A-Z]{3}\d{8}$")
    for idx, row in valid_df.iterrows():
        sn = row["serial_clean"]
        if not serial_pattern.match(sn):
            exceptions.append({
                "row_number": idx + 2,
                "serial_number": sn,
                "issue_type": "Invalid Format",
                "details": "Expected format: 3 uppercase letters + 8 digits (e.g., TRM10293847)."
            })

    # 4. Active units missing a location assignment
    active_unassigned = valid_df[
        (valid_df["status"].astype(str).str.strip().str.lower() == "active") &
        (valid_df["location_id"].isna() | (valid_df["location_id"].astype(str).str.strip() == ""))
    ]
    for idx, row in active_unassigned.iterrows():
        exceptions.append({
            "row_number": idx + 2,
            "serial_number": row["serial_clean"],
            "issue_type": "Unassigned Active Unit",
            "details": "Terminal status is 'Active' but location_id is blank."
        })

    # Export findings if anomalies exist
    if exceptions:
        report_df = pd.DataFrame(exceptions)
        report_df.to_excel(output_report, index=False)

    summary = {
        "audit_timestamp": datetime.utcnow().isoformat() + "Z",
        "total_records_scanned": len(df),
        "total_exceptions_found": len(exceptions),
        "report_generated": output_report if exceptions else None
    }
    return summary


if __name__ == "__main__":
    # Example execution
    SAMPLE_INPUT = "data/terminal_inventory_q4.xlsx"
    try:
        result = audit_serial_inventory(SAMPLE_INPUT)
        print("Audit Complete:", result)
    except Exception as error:
        print(f"Audit aborted: {error}")
