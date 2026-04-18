# Copyright (c) 2026 Victor Roberto Serranoni da Costa. All rights reserved. Registered with INPI.
import os
import json
import hashlib
import zlib

class DataEquityCollector:
    def __init__(self, storage_path="data/output/"):
        self.storage_path = storage_path
        if not os.path.exists(self.storage_path):
            os.makedirs(self.storage_path)

    def process_collected_data(self, raw_data):
        data_str = json.dumps(raw_data)
        file_id = hashlib.sha256(data_str.encode()).hexdigest()
        compressed_data = zlib.compress(data_str.encode(), level=9)
        filename = f"{file_id}.eqty"
        full_path = os.path.join(self.storage_path, filename)
        with open(full_path, "wb") as f:
            f.write(compressed_data)
        return file_id, full_path
