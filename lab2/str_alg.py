def transform_str(str):
    return str[::2]

str_1="hello, Jooohn"
str_2="hodo, ik"

print(str_1 + " -> " + transform_str(str_1))
print(str_2 + " -> " + transform_str(str_2))
