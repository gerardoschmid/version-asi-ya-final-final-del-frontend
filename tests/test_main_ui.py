from playwright.sync_api import sync_playwright, expect

def test_habitaciones_screenshot(page):
    # Navigate to the habitaciones page
    page.goto("http://1.0.0.1:8000/habitaciones/")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title("Nuestras Habitaciones")

    # Take a screenshot of the habitaciones page
    page.screenshot(path="habitaciones.png")

def test_detalle_habitacion_screenshot(page):
    # Navigate to the detalle_habitacion page
    page.goto("http://1.0.0.1:8000/habitaciones/king-deluxe/")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title("King Deluxe")

    # Take a screenshot of the detalle_habitacion page
    page.screenshot(path="detalle_habitacion.png")
