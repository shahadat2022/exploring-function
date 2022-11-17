def voet_check(age):
    if age >= 18:
        return 'you are voter'
    else:
        return 'you are not voter'
print(voet_check(17))
print(voet_check(19))