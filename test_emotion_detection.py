from EmotionDetection import emotion_detector

def test_emotions():
    tests = [
        ("I am glad this happened", "joy"),
        ("I am really mad about this", "anger"),
        ("I feel disgusted just hearing about this", "disgust"),
        ("I am so sad about this", "sadness"),
        ("I am really afraid that this will happen", "fear")
    ]

    passed = 0
    failed = 0

    for statement, expected in tests:
        result = emotion_detector(statement)
        dominant = result.get('dominant_emotion') if result else 'None'
        if dominant == expected:
            print(f"✅ Passed: \"{statement}\" → {dominant}")
            passed += 1
        else:
            print(f"❌ Failed: \"{statement}\" → Expected: {expected}, Got: {dominant}")
            failed += 1

    print(f"\nTest summary: {passed} passed, {failed} failed")

# Run the test function
if __name__ == "__main__":
    test_emotions()
