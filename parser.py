import re
import os

file_path = r"C:\Users\dhanyashree\Downloads\Production_SCAN_stuck_at_Example (3).stil"

print("Path exists:", os.path.exists(file_path))

def parse_stil(file_path):
    with open(file_path, 'r', errors='ignore') as f:
        data = f.read()

    print("File loaded, length:", len(data))

    total_patterns = len(re.findall(r'\bPattern\b', data))
    scan_chains = len(re.findall(r'\bScanChain\b', data))

    scan_lengths = re.findall(r'ScanLength\s+(\d+)', data)
    scan_lengths = list(map(int, scan_lengths))

    if scan_lengths:
        scan_length_per_chain = scan_lengths[0]
    else:
        scan_length_per_chain = 0

    total_ff = sum(scan_lengths)

    return {
        "total_patterns": total_patterns,
        "scan_chains": scan_chains,
        "scan_length": scan_length_per_chain,
        "total_ff": total_ff
    }

result = parse_stil(file_path)
print("RESULT:", result)