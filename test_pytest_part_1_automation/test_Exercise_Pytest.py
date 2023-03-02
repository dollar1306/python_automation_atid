class Test_Pytest:
    def setup_class(self):
        print("\nRun before tests")

    def teardown_class(self):
        print("Run after class")

    def setup_method(self):
        print("Before Test Case")

    def teardown_method(self):
        print("After Test Case")

    def test_1(self):
        print("Test Case 1")

    def test_2(self):
        print("Test Case 2")
