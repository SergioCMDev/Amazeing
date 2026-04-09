mandatory_keys: set[str] = {"WIDTH", "HEIGHT", "ENTRY", "EXIT", "OUTPUT_FILE",
                            "PERFECT"}

valid_keys: set[str] = mandatory_keys.union("Test")
