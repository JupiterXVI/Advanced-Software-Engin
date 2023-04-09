input_fields = [
    {
        "username" : "1",
        "password" : "1",
        "passwort_repeat" : "1"
    },
    {
        "username" : "1",
        "password" : "1",
        "passwort_repeat" : "1"
    },
    {
        "username" : "1",
        "password" : "1",
        "passwort_repeat" : "1"
    }]

input_fields2 = [
    {
        "username" : "2",
        "password" : "2",
        "passwort_repeat" : "2"
    },
    {
        "username" : "2",
        "password" : "2",
        "passwort_repeat" : "2"
    },
    {
        "username" : "2",
        "password" : "2",
        "passwort_repeat" : "2"
    }]

print(input_fields + input_fields2)
print()
print(input_fields.extend(input_fields2))