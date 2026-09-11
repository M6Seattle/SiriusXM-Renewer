    print("Creating Account...")
    result = createAccount()
    if result[1] == 200:
        print(f"DEBUG: Response structure: {result[2]}\n")
        # Check if response has an error status
        if "opstatus" in result[2]:
            if result[2]["opstatus"] != 0:  # 0 = success
                print(f"Error creating account: {result[2].get('errmsg', 'Unknown error')}\n")
                alreadyActive = True
            else:
                print("Account Created\n")
        elif "resultData" in result[2]:
            if result[2]["resultData"][0]["resultCode"] == "FAILURE":
                if result[2]["resultData"][2]["message"]  == "Device ID is already active":
                    print("\nThis car has already been registered and is still currently active. Please try again later.\n")
                    alreadyActive = True
                else:
                    print(f"\nError: {result[2]["resultData"][2]["message"]}\n")
                    alreadyActive = True
            else:
                print("Account Created\n")
        else:
            print(f"Unexpected response format: {result[2]}\n")
    else:
        print(f"!!Account Created Unsuccessfully!! Status Code: {result[1]}\n")
        exit()
