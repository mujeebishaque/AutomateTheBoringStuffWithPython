
name = "David"
job = "Analyst"
company = "TechLead"

print("Hello %s. Are you an %s at %s" %(name, job, company))
user_input = input()

try:
    if str(user_input) == "yes" or str(user_input) == "YES":
        print("Welcome aboard")
except ValueError:
    print("ERROR: String input required")
