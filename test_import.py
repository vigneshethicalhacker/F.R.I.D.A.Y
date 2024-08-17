from utils.speech import Speech

def test_import():
    try:
        speech = Speech()
        print("Import successful!")
    except ImportError as e:
        print(f"Import failed: {e}")

if __name__ == "__main__":
    test_import()
