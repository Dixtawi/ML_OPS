import pytest
from config import MODEL_PATH
import joblib

def test_predict_price():
    model = joblib.load(MODEL_PATH)
    features = [8960, 4, 4, 4, 1, 0, 0, 0, 1, 3, 0, 0]
    expected_price = 12250000
    tolerance = 1000000

    result = round(model.predict([features])[0])
    assert expected_price - tolerance <= result <= expected_price + tolerance, (
        f"Expected price to be within ±{tolerance} of {expected_price}, "
        f"but got {result}"
    )

    print(result)
