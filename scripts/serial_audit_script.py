"""
Title: Enterprise POS Terminal Serial-Number Audit & Anomaly Detection Pipeline
Author: Mustapha Abiodun Oyeyemi
Purpose: Optimized pandas/numpy script designed to audit, clean, and reconcile 
         large-scale hardware inventories exceeding 15,000+ terminal records.
"""

import numpy as np
import pandas as pd


def audit_enterprise_terminal_fleet(file_path):
    print("--- Starting Enterprise Fleet Audit (15,000+ Units) ---")

    try:
        # Optimized loading: read only required columns to save memory on massive files
        use_cols = ["Terminal_ID", "Status", "Model", "Batch_ID", "Deployment_Date"]
        df = pd.read_excel(file_path, usecols=use_cols)
    except FileNotFoundError:
        print(f"File {file_path} not found. Generating large-scale synthetic benchmark (15,000+ records)...")
        
        # Simulate 15,000+ records using numpy for standalone portfolio benchmarking
        np.random.seed(42)
        n_records = 15420
        
        models = ["Ingenico 8210", "Ingenico 8110", "Nexgo K320"]
        statuses = ["Deployed", "Repaired", "Pending Parts", "Unassigned"]
        
        mock_data = {
            "Terminal_ID": [f"POS-{np.random.choice([8210, 8110, 320])}-{str(i).zfill(5)}" for i in range(n_records)],
            "Status": np.random.choice(statuses, size=n_records, p=[0.6, 0.2, 0.1, 0.1]),
            "Model": np.random.choice(models, size=n_records, p=[0.4, 0.3, 0.3]),
            "Batch_ID": [f"BATCH-{np.random.randint(100, 150)}" for _ in range(n_records)]
        }
        df = pd.DataFrame(mock_data)
        
        # Inject intentional duplicate serials and anomalies for QA testing
        df.loc[100, "Terminal_ID"] = df.loc[50, "Terminal_ID"]
        df.loc[500, "Terminal_ID"] = "INVALID_SERIAL_FORMAT"

    print(f"Total Fleet Records Loaded: {len(df):,}")

    # 1. Vectorized Duplicate Detection (O(n) performance)
    duplicate_mask = df.duplicated(subset=["Terminal_ID"], keep=False)
    duplicate_count = duplicate_mask.sum()
    print(f"\n[Data QA Anomaly Check] Detected {duplicate_count:,} duplicate serial numbers.")

    # 2. Flagging Formatting / Validation Anomalies
    invalid_mask = df["Terminal_ID"].str.contains("INVALID|UNKNOWN|NULL", na=True)
    invalid_count = invalid_mask.sum()
    print(f"[Validation Check] Flagged {invalid_count:,} records with invalid serial formatting.")

    # 3. Fleet Status Breakdown & Aggregation
    fleet_summary = df.groupby(["Model", "Status"]).size().unstack(fill_value=0)
    print("\n[Summary] Enterprise Fleet Status Breakdown:")
    print(fleet_summary)

    print("\n--- Enterprise Audit Pipeline Executed Successfully ---")
    return df


if __name__ == "__main__":
    audit_enterprise_terminal_fleet("enterprise_terminal_master_log.xlsx")
