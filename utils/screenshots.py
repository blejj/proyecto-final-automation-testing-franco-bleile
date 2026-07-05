import os
from datetime import datetime


def take_screenshot(driver, test_name):

    # Crear carpeta si no existe
    if not os.path.exists("screenshots"):
        os.makedirs("screenshots")

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    file_name = f"{test_name}_{timestamp}.png"

    path = os.path.join("screenshots", file_name)

    driver.save_screenshot(path)

    return path