import os
import base64
import argparse
import hashlib

# PROJECT SHATTEREDGLASS IOCHUNTER v2.0 (DeepSeek-V4-Flash Patched)
# Advanced detection for hardware-anchored persistence and activation bypass

IO_PATTERNS = {
    "activation_bypass_binary": b"7u7u7u7u7u",
    "activation_bypass_b64": "ADDu7u7u7x", # Common B64 variant in logs
    "cert_serial": "0b745972d0f5e989",
    "cert_fingerprint": "1acd2cad357e18167faf30b55ef83ced0997ddd1",
    "fdr_seal_anomaly": "07/10/2022",
    "c2_domain": "weather-map2.apple.com",
    "python_payload": "pydub",
    }

def scan_file(file_path):
    hits = []
    try:
        with open(file_path, 'rb') as f:
            content = f.read()
            
            # 1. SHA1 Fingerprinting for binary .der files
            if file_path.endswith('.der'):
                file_hash = hashlib.sha1(content).hexdigest()
                if file_hash == IO_PATTERNS["cert_fingerprint"]:
                    hits.append(f"[CRITICAL] MATCH: ShatteredGlass Certificate Fingerprint Detected")

            # 2. Binary Pattern Scanning (7u7u)
            if IO_PATTERNS["activation_bypass_binary"] in content:
                hits.append(f"[CRITICAL] Found Legacy Activation Bypass Binary Pattern (7u7u)")
            
            # 3. Text-Based Indicator Scanning
            text_content = content.decode('utf-8', errors='ignore')
            
            if IO_PATTERNS["activation_bypass_b64"] in text_content:
                hits.append(f"[CRITICAL] Found Activation Bypass Base64 Pattern (7u7u variant)")
            
            if IO_PATTERNS["fdr_seal_anomaly"] in text_content and "FDR" in file_path:
                hits.append(f"[HIGH] Found FDR 'Time-Travel' SealDate Anomaly (2022)")

            if IO_PATTERNS["cert_serial"] in text_content:
                hits.append(f"[HIGH] Found ShatteredGlass Certificate Serial: {IO_PATTERNS['cert_serial']}")
            
            if IO_PATTERNS["c2_domain"] in text_content:
                hits.append(f"[HIGH] Found C2 Domain: {IO_PATTERNS['c2_domain']}")
            
            if IO_PATTERNS["python_payload"] in text_content:
                hits.append(f"[SUSPICIOUS] Found Python/pydub exfiltration logic")
            
            if IO_PATTERNS["local_peer"] in text_content:
                hits.append(f"[SUSPICIOUS] Found Local Peer IP: {IO_PATTERNS['local_peer']}")

    except Exception:
        pass
    return hits

def main():
    parser = argparse.ArgumentParser(description="ShatteredGlass IoC Scanner v2.0")
    parser.add_argument("directory", help="Directory to scan (backups, logs, etc.)")
    args = parser.parse_args()

    print("=" * 60)
    print("PROJECT SHATTEREDGLASS: FORENSIC IOCHUNTER v2.0")
    print("=" * 60)
    print(f"[*] Target: {args.directory}")
    print("[*] Monitoring for hardware-anchored persistence signatures...")

    hit_count = 0
    for root, _, files in os.walk(args.directory):
        for file in files:
            file_path = os.path.join(root, file)
            hits = scan_file(file_path)
            if hits:
                hit_count += 1
                print(f"\n[!] ALERT: {file_path}")
                for hit in hits:
                    print(f"    - {hit}")

    print("\n" + "=" * 60)
    print(f"[*] Scan Complete. Total Matches: {hit_count}")
    print("=" * 60)

if __name__ == "__main__":
    main()

