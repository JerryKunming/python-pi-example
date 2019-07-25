is_male = True
is_tall = False

if is_male:
    print("You are a male.")
else:
    print("You are not a male.")

if is_male or is_tall:
    print("You are a male or you are tall or both.")
else:
    print("You are neither a male nor tall.")

if is_male and is_tall:
    print("You are a tall male.")
elif is_male and not(is_tall):
    print("You are a short male.")
elif not(is_male) and is_tall:
    print("You are a tall woman.")
else:
    print("You are a short woman.")


