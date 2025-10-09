def check_password():
    submitted_password = str(input("Password: "))

    real_password = "Knights25"
    if real_password == submitted_password:
        print("Access Granted")

    else:
        print("Access Denied")
        check_password()


check_password()