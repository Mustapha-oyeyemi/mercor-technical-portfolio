# Standard Operating Procedure: POS Terminal Audit & Maintenance
**Document ID:** SOP-POS-042  
**Author:** Mustapha Abiodun Oyeyemi  
**Target Hardware:** Ingenico (8110, 8210) & Nexgo K320 Terminals  

---

## 1. Purpose & Objective
To establish a rigorous, repeatable protocol for auditing, diagnosing, repairing, and reconciling POS terminal hardware to ensure zero unassigned serial discrepancies and optimal battery/printer performance.

## 2. Pre-Audit Equipment Setup
- ESD-safe workstation with calibrated multimeter and stable DC power supply.
- Master Excel/Python audit template loaded with current inventory serial numbers.

## 3. Step-by-Step Execution Protocol
1. **Physical Inspection:** Check casing integrity, keypad responsiveness, and thermal printer roller assembly.
2. **Serial Number Verification:** Scan barcode/IMEI against the master inventory database to prevent duplicate logging.
3. **Diagnostic Bench Testing:**
   - Execute battery stress test (minimum 80% charge retention benchmark).
   - Test SIM module and network signal handshake (4G/GPRS).
4. **Data Reconciliation:** Log repair status (`Deployed`, `Repaired`, `Pending Parts`, or `Scrapped`) into the tracking sheet immediately upon test completion.

## 4. Quality Control & Reporting
- Compile weekly summaries highlighting failure trends (e.g., thermal head wear vs. battery degradation).
- Submit audit logs to maintenance supervisors for sign-off prior to release.
