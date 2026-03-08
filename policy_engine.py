def access_decision(score):

    if score < 20:
        return "Full Access Granted"

    elif score < 50:
        return "Access with MFA Required"

    elif score < 70:
        return "Restricted Access"

    else:
        return "Access Denied"