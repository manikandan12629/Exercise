# myDict = {
#     1: "mani",
#     2: "suresh"
# }

#print(myDict)
import random
import string
random_invalid_alnums = lambda s="rand12", exclude=[]: [
    str(s) + c for c in string.punctuation if c not in exclude
]
random_invalid_alphas = lambda s="rand", exclude=[]: [
    str(s) + c for c in string.punctuation + string.digits[:2] if c not in exclude
]
random_invalid_numbers = lambda s=12, exclude=[]: [
    str(s) + c
    for c in string.punctuation + string.ascii_letters[:2]
    if c not in exclude
]

print(random_invalid_alnums())
invalid_values_for_fields = {
    "client": ["AA" * 6] + ["RPOSs", "Personify"],
    "communicationType": random_invalid_alphas() + ["AA" * 16],
    "contactId": random_invalid_alnums(exclude="'-") + ["AA" * 16],
    "templateId": random_invalid_alnums() + ["AA" * 51],
    "sourceAddress": random_invalid_numbers() + ["9" * 9, "9" * 21],
    "recipientAddress": random_invalid_numbers() + ["9" * 9, "9" * 21],
    "transactionType": random_invalid_alphas(exclude="'-") + ["AA" * 26],
    "contactPhonenumber": random_invalid_numbers() + ["9" * 9, "9" * 21],
}

print(invalid_values_for_fields)
