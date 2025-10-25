# Project: Web Application Manual Testing (E-commerce Website)
# Author: [Your Name]
# Description:
# This project demonstrates manual testing for an e-commerce website.
# It includes a test plan, sample test cases, and sample bug reports.

def project_intro():
    print("=====================================================")
    print("     WEB APPLICATION MANUAL TESTING PROJECT")
    print("              E-COMMERCE WEBSITE")
    print("=====================================================\n")

def test_plan():
    print("📘 TEST PLAN")
    print("-----------------------------------------------")
    print("1. Objective:")
    print("   To verify that all the functionalities of the E-commerce website")
    print("   (login, search, add to cart, checkout) work as expected.\n")
    
    print("2. Scope:")
    print("   - Functional Testing")
    print("   - UI Testing")
    print("   - Usability Testing")
    print("   - Compatibility Testing\n")

    print("3. Test Environment:")
    print("   - Browser: Chrome v120+")
    print("   - OS: Windows 10")
    print("   - URL: https://demo.opencart.com/\n")

def test_cases():
    print("🧪 SAMPLE TEST CASES")
    print("-----------------------------------------------")

    print("Test Case 1: Verify Login Functionality")
    print("------------------------------------------------")
    print("Test ID: TC001")
    print("Module: Login")
    print("Test Steps:")
    print("  1. Navigate to Login Page")
    print("  2. Enter valid email and password")
    print("  3. Click 'Login' button")
    print("Expected Result: User should be redirected to Dashboard.\n")

    print("Test Case 2: Verify Add to Cart Functionality")
    print("------------------------------------------------")
    print("Test ID: TC002")
    print("Module: Cart")
    print("Test Steps:")
    print("  1. Search for a product")
    print("  2. Click 'Add to Cart'")
    print("Expected Result: Product should be added to cart successfully.\n")

    print("Test Case 3: Verify Checkout Functionality")
    print("------------------------------------------------")
    print("Test ID: TC003")
    print("Module: Checkout")
    print("Test Steps:")
    print("  1. Open cart with product added")
    print("  2. Proceed to checkout")
    print("  3. Fill valid billing details")
    print("Expected Result: Order should be placed successfully.\n")

def bug_reports():
    print("🐞 SAMPLE BUG REPORTS")
    print("-----------------------------------------------")

    print("Bug ID: BUG001")
    print("Title: 'Add to Cart' button not working on product page")
    print("Severity: High")
    print("Steps to Reproduce:")
    print("  1. Open any product page")
    print("  2. Click on 'Add to Cart'")
    print("Expected: Product should be added to cart")
    print("Actual: Nothing happens")
    print("Status: Open\n")

    print("Bug ID: BUG002")
    print("Title: 'Login' accepts invalid credentials")
    print("Severity: Critical")
    print("Steps to Reproduce:")
    print("  1. Go to Login Page")
    print("  2. Enter invalid credentials")
    print("Expected: Error message should appear")
    print("Actual: User gets redirected to Dashboard")
    print("Status: Open\n")

def conclusion():
    print("✅ CONCLUSION")
    print("-----------------------------------------------")
    print("The manual testing of the E-commerce website helped identify")
    print("critical bugs in login and add-to-cart modules.")
    print("Further regression and retesting are planned after fixes.\n")
    print("=====================================================")
    print("End of Project Report")
    print("=====================================================")

# Run all sections
project_intro()
test_plan()
test_cases()
bug_reports()
conclusion()
