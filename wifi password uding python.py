import subprocess

def get_wifi_profiles():
    try:
        result = subprocess.check_output(["netsh", "wlan", "show", "profiles"]).decode("utf-8")
        profiles = [line.split(":")[1].strip() for line in result.split("\n") if "All User Profile" in line]
        return profiles
    except subprocess.CalledProcessError:
        print("Error retrieving Wi-Fi profiles.")
        return []

def get_wifi_password(profile):
    try:
        result = subprocess.check_output(["netsh", "wlan", "show", "profile", profile, "key=clear"]).decode("utf-8")
        password_lines = [line.strip() for line in result.split("\n") if "Key Content" in line]
        if password_lines:
            return password_lines[0].split(":")[1].strip()
        else:
            return "Password not found."
    except subprocess.CalledProcessError:
        return "Error retrieving password."

def main():
    wifi_profiles = get_wifi_profiles()
    for profile in wifi_profiles:
        password = get_wifi_password(profile)
        print(f"Wi-Fi Network: {profile} | Password: {password}")

if __name__ == "__main__":
    main()

                                                                                          
                                                                                          