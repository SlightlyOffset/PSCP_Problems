'''BloodDonation'''
def main():
    '''BloodDonation'''
    age = int(input())
    weight = int(input())
    donated = int(input())

    check_for_permission_or_cert = bool(age == 17 or 60 <= age <= 70)
    if check_for_permission_or_cert:
        permission_or_cert = input().lower() == 'true'

    pass_age = 17 <= age <= 70
    pass_weight = weight >= 45
    pass_donated = (not donated and age <= 55) or (donated > 0)
    if check_for_permission_or_cert: # If permission or certificate is required
        # It simply means permission_or_cert must be True
        pass_permission_or_cert = permission_or_cert

    criteria = [pass_age, pass_weight, pass_donated]
    if check_for_permission_or_cert:
        criteria.append(pass_permission_or_cert)
    print("Yes" if all(criteria) else "No")

if __name__ == "__main__":
    main()
