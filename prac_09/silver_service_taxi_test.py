from silver_service_taxi import SilverServiceTaxi

def test_init():
    """Check that the SilverServiceTaxi initializes with correct attribute values"""
    taxi = SilverServiceTaxi("Lexus", 150, 3.0)
    assert taxi.name == "Lexus", "Name not set properly"
    assert taxi.fuel == 150, "Fuel value incorrect"
    assert abs(taxi.price_per_km - (1.23 * 3.0)) < 0.01, "Price per km not calculated correctly"
    assert taxi.flagfall == 4.50, "Flagfall amount is wrong"
    print("Initialization test passed")

def test_get_fare():
    """Verify fare is computed correctly for a 10km journey at fanciness level 3"""
    taxi = SilverServiceTaxi("Lexus", 150, 3.0)
    taxi.start_fare()  # Begin a new fare
    taxi.drive(10)  # Simulate driving 10 km
    expected_fare = (1.23 * 3.0 * 10) + 4.50  # Fare = distance * rate + flagfall
    actual_fare = taxi.get_fare()
    assert abs(actual_fare - 41.40) < 0.01, f"Expected fare $41.40, got ${actual_fare:.2f}"
    print("Fare calculation test passed")

def test_str():
    """Confirm that the string output includes all key details including flagfall"""
    taxi = SilverServiceTaxi("Lexus", 150, 3.0)
    expected_str = f"Lexus, fuel=150, odometer=0, 0km on current fare, ${1.23 * 3.0:.2f}/km plus flagfall of 4.50"
    assert str(taxi) == expected_str, "String format output is incorrect"
    print("String representation test passed")

if __name__ == "__main__":
    test_init()
    test_get_fare()
    test_str()
    print("All tests completed")
