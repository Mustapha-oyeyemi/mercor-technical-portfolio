"""
Title: Anonymized POS Terminal Serial-Number Audit & Anomaly Detection Script
Author: Mustapha Abiodun Oyeyemi
Purpose: Automates data validation, duplicate checking, and reconciliation 
         across large-scale hardware inventory logs using pandas and openpyxl.
"""

import pandas as pd


def audit_terminal_inventory(file_path):
    print("--- Starting Terminal Inventory Audit ---")

    # Load dataset
    try:
        df = pd.read_excel(file_path)
    except FileNotFoundError:
        print(f"Error: File {file_path} not found. Running mock audit demo...")
        # Mock dataframe for demonstration
        data = {
            "Terminal_ID": [
                "POS-8210-001",
                "POS-8210-002",
                "POS-8210-001",
                "K320-501",
                "K320-502",
                "INVALID_SN",
            ],
            "Status": [
                "Deployed",
                "Repaired",
                "Deployed",
                "Pending",
                "Faulty",
                "Unknown",
            ],
            "Model": ["8210", "8210", "8210", "K320", "K320", "Unknown"],
        }
        df = pd.DataFrame(data)

    # 1. Detect Duplicate Serial Numbers
    duplicates = df[df.duplicated(subset=["Terminal_ID"], keep=False)]
    print(
        f"\n[Anomaly Check] Found {len(duplicates)} duplicate terminal records."
    )

    # 2. Flag Unassigned / Invalid Models
    invalid_units = df[df["Model"] == "Unknown"]
    print(
        f"[Validation Check] Found {len(invalid_units)} records with unverified models."
    )

    # 3. Summary Statistics by Status
    status_summary = df["Status"].value_counts()
    print("\n[Summary] Terminal Status Breakdown:")
    print(status_summary)

    print("\n--- Audit Complete Successfully ---")
    return df


if __name__ == "__main__":
    audit_terminal_inventory("terminal_master_log.xlsx")
