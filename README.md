# Project Shattered-Glass: Hardware-Anchored iOS Persistence

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Type](https://img.shields.io/badge/sector-Forensics-red.svg)
![Status](https://img.shields.io/badge/status-CONCLUDED-success.svg)

## Overview
**Project Shattered-Glass** is a forensic investigation into a hardware-anchored implant that achieves permanent persistence on modern iOS devices. By subverting the physical identity (FDR) and re-anchoring the root-of-trust in the silicon registers, the implant renders all software-based restores, including DFU, obsolete.

##  The Forensic Engineering Workstation
The centerpiece of this disclosure is the interactive **Forensic Engineering Workstation**. 

### **[>> CLICK HERE TO LAUNCH THE INTERACTIVE DASHBOARD <<](https://htmlpreview.github.io/?https://github.com/JGOYD/Shattered-Glass/blob/main/index.html)**


### Features:
- **Visualizes the Exploit Chain**: High-precision mapping of the FDR -> SEP -> Kernel hijack.
- **Verification Engine**: Functional drag-and-drop ingestion to scan sysdiagnose logs for fingerprints (7u7u, SKI hashes, SealDate anomalies) in real-time.
- **Telemetry Monitoring**: Real-time status of hijacked J-series registers and the unsealed eCfg bond.

## Key Technical Findings
- **Hardware Persistence**: Survived deep DFU restore via FDR/NVRAM register manipulation.
- **Bypass**: Utilizes legacy activation certificates (2007-2014) and synthetic "7u7u" binary wildcard tickets.
- **Cover**: Hijacks system extensions and iCloud Private Relay (ODoH) for stealthy C2 communication.

## Repository Structure
- /Advisory: The [Full Vulnerability Report](./Shattered-Glass_Vulnerability_Report.md).
- /Manifesto: The [Exploit Manifesto](./Shattered-Glass_Exploit_Manifesto.md) for universal hardware persistence.
- /Evidence: The [Technical Evidence Ledger](./Shattered-Glass_Evidence_Ledger.md) containing raw hex and log proof.
- /Tools: shattered-glass_scanner.py (v2.0) for automated IoC detection.

## Detection
Security researchers can verify their own device integrity by dropping a sysdiagnose into the Workstation (index.html) or by running the CLI tool:
`ash
python tools/shattered-glass-scanner.py path/to/sysdiagnose
`

---
