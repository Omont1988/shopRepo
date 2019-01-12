import pytest
from tests.fixture.session import Session
import tests.helpers.report as utils


# Create driver and url command line addoption
def pytest_addoption(parser):
    parser.addoption("--url", action="store", default="http://web:8080", help="url")


browser = None


# Create driver fixture that initiates chrome
@pytest.fixture(scope="session", autouse=True)
def driver(request):
    global browser
    if browser is None:
        browser = Session()
        request.addfinalizer(browser.close_session())
        return browser.wd
    else:
        if browser.is_valid() is not True:
            browser = Session()
            request.addfinalizer(browser.close_session())
            return browser.wd

# # Screenshot in case of any test failure
# def pytest_exception_interact(node, report):
#     if node and report.failed:
#         class_name = node._nodeid.replace(".py::", "_class_")
#         name = "{0}_{1}".format(class_name, url)
#         utils.save_screenshot(node.funcargs.get("driver"), name)


# Create url fixture
@pytest.fixture(scope="session")
def url(request):
    return request.config.getoption("--url")
