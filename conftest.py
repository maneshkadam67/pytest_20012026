def pytest_runtest_setup(item):

    """this is newly added code"""
    print("**",item.nodeid,"***************this is before")

