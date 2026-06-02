# Project ShatteredGlass: Hardware-Anchored iOS Persistence

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Type](https://img.shields.io/badge/sector-Forensics-red.svg)

## Overview
**Project ShatteredGlass** is a forensic investigation into a hardware-anchored implant that achieves persistence on modern iOS devices by subverting the device's identity (FDR) and activation sequence.

## Key Findings
- **Persistence**: Survives DFU restore via NVRAM/FDR-level identity spoofing.
- **Bypass**: Utilizes legacy activation certificates and synthetic "7u7u" wildcard tickets.
- **Cover**: Hijacks system extensions and iCloud Private Relay (ODoH) for stealthy C2 communication.

## Repository Contents
- `/Advisory`: The [Full Vulnerability Report](./SHATTEREDGLASS_VULNERABILITY_REPORT.md).
- `/Evidence`: The [Technical Evidence Ledger](./SHATTEREDGLASS_EVIDENCE_LEDGER.md).
- `/Tools`: `shatteredglass_scanner.py` for automated IoC detection in sysdiagnoses.
- `/Visuals`: [Interactive 3D Threat Map (HTML)](./SHATTEREDGLASS_DASHBOARD.html) and [Trust Hijack Sequence](./SHATTEREDGLASS_TRUST_HIJACK_VISUAL.md).

## Detection
Users can verify their own sysdiagnose logs using the provided scanner:
```bash
python tools/shatteredglass_scanner.py path/to/sysdiagnose
```

## Attribution
This exploit chain is linked to state-sponsored actors utilizing the an Apple signed certificate.

---

