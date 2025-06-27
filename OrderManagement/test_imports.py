import sys
import os

# Add current (root) folder to sys.path
project_root = os.path.abspath(os.path.dirname(__file__))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

print("\n sys.path contents:")
for p in sys.path:
    print("  -", p)

print("\n Trying to import OrderProcessor...")
try:
    from dao.order_processor import OrderProcessor
    print("Import worked: OrderProcessor loaded.")
except Exception as e:
    print(" Import failed:", e)
