'''BloodDonation'''
def main():
    '''BloodDonation'''
    age = int(input())
    weight = int(input())
    donated = int(input())

    # All base conditions must be met.
    # 1. Age must be between 17 and 70.
    # 2. Weight must be at least 45.
    # 3. First-time donors (donated == 0) must be 55 or younger.
    #    If they have donated before (donated > 0), this condition is met.
    is_eligible = (17 <= age <= 70) and \
                  (weight >= 45) and \
                  (donated > 0 or (not donated and age <= 55))

    # Special age groups (17 or 60-70) require an additional permission check.
    if is_eligible and (age == 17 or 60 <= age <= 70):
        has_permission = input().lower() == 'true'
        is_eligible = has_permission

    print("Yes" if is_eligible else "No")

if __name__ == "__main__":
    main()
