from playwright.sync_api import sync_playwright, expect

def test_admin_screenshot(page):
    # Navigate to the admin login page
    page.goto("http://127.0.0.1:8000/admin/login/")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title("Log in | Django site admin")

    # Fill in the login form
    page.fill('input[name="username"]', 'admin')
    page.fill('input[name="password"]', 'adminpassword')

    # Click the login button
    page.click('input[type="submit"]')

    # Wait for navigation to the dashboard
    page.wait_for_url("http://127.0.0.1:8000/admin/")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title("Site administration | Django site admin")

    # Take a screenshot of the admin dashboard
    page.screenshot(path="admin_dashboard.png")
