mandatory_keys: set[str] = {"WIDTH", "HEIGTH", "ENTRY", "EXIT", "OUTPUT_FILE",
                            "PERFECT"}

valid_keys: set[str] = mandatory_keys.union("Test")
