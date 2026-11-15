# Standard Operating Procedure: POS & Field Terminal Preventive Maintenance

**Document ID:** SOP-OPS-042  
**Version:** 2.1  
**Effective Date:** October 2026  
**Owner:** Technical Field Operations  

---

## 1. Purpose
To establish a standardized, repeatable procedure for inspecting, sanitizing, updating, and verifying point-of-sale (POS) and field data terminals. Adherence to this SOP prevents hardware downtime, eliminates firmware drift, and ensures accurate asset tracking.

## 2. Scope
Applies to all Tier-1 and Tier-2 field technicians performing scheduled quarterly maintenance or pre-deployment staging on ruggedized handheld and countertop terminals.

## 3. Required Tools & Materials
* Microfiber lint-free cloths and 70% isopropyl alcohol wipes
* Compressed air canister (moisture-free)
* Digital multimeter (for cradle/dock voltage verification)
* Encrypted diagnostic USB-C drive loaded with the latest approved firmware image
* Asset barcode scanner / mobile inventory app

---

## 4. Safety & Pre-Check Precautions
> **Warning:** Power down the terminal completely and disconnect all external AC/DC power sources before cleaning internal contacts or swapping battery packs. Never spray liquids directly onto screens, card slots, or ports.

---

## 5. Step-by-Step Procedure

### Phase 1: Physical & Hardware Inspection
1. **Verify Asset Identity:** Scan the chassis barcode and confirm the physical serial number matches the active deployment log (format: `TRM` + 8 digits). Flag any discrepancy immediately.
2. **Inspect Casing & Display:** Check for housing cracks, swollen battery covers, or touchscreen dead zones.
3. **Clean Card Readers & Ports:**
   * Use compressed air to clear debris from the USB-C charging port, SIM/SAM tray, and smart-card slot.
   * Run a pre-saturated cleaning card through the magnetic stripe/EMV reader three times.
4. **Sanitize Exterior:** Wipe the display and keypad with a lightly dampened 70% isopropyl alcohol cloth and allow 60 seconds to air dry.

### Phase 2: Power & Battery Diagnostics
1. Power on the terminal and enter **Diagnostic Mode** (`Power + Volume Down` for 5 seconds).
2. Navigate to **Battery Health** and verify:
   * **State of Health (SoH):** Must be $\ge 80\%$. Replace any battery below this threshold.
   * **Charging Current:** Dock the unit and confirm stable input voltage ($5.0\text{ V} \pm 0.25\text{ V}$).

### Phase 3: Firmware & Connectivity Verification
1. Compare the installed OS build against the current approved baseline in the release registry.
2. If outdated, connect the diagnostic USB-C drive and execute the signed update package. **Do not interrupt power during flashing.**
3. Run the automated network test suite to verify:
   * Wi-Fi / Cellular signal lock
   * TLS 1.3 handshake with the central telemetry server
   * Receipt printer test-page output (if applicable)

---

## 6. Post-Maintenance Sign-Off & Escalation

| Condition Found | Required Action | Escalation SLA |
| :--- | :--- | :--- |
| All checks pass | Log completion timestamp and technician ID in the asset portal; return unit to service. | N/A |
| Battery SoH $< 80\%$ | Swap with calibrated spare battery; tag depleted unit for e-waste recycling. | Same visit |
| Damaged port / failed TLS check | Quarantine unit with a **Red Out-of-Service Tag**, issue a swap terminal, and open a Tier-3 RMA ticket. | Within 4 hours |
