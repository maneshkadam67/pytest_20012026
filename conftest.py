def pytest_runtest_setup(item):
    print("**",item.nodeid,"***************this is before")
