# AND Operator &
Resultado1 = True & True    # Nos devuelve True
Resultado2 = False & True   # Nos devuelve False
Resultado3 = True & False   # Nos devuelve True
Resultado4 = False & False  # Nos devuelve False

# OR Operator |
Resultado5 = True | True    # Nos devuelve True
Resultado6 = False | True   # Nos devuelve True
Resultado7 = True | False   # Nos devuelve True
Resultado8 = False | False  # Nos devuelve False

# NOT Operator
Resultado9 = not True     # Nos devuelve un False
Resultado10 = not False   # Nos devuelve un True

# Exercise 1. Credential validator with AND &
usuario_correcto = True
contraseña_correcta = False

allowed_access = usuario_correcto & contraseña_correcta
print(allowed_access)

# Execise 2. Weekend discount validator (using "OR").
monday = False
tuesday = False
wednesday = False
thursday = False
friday = False
saturday = True
sunday = True

discount_day = saturday or sunday
print(discount_day)

# Exercise 3. Inverting a Boolean with not
switch_off = False
switch_on = True

turn_light = not switch_off
print(turn_light)

# Exercise 4. Number Range Check (10 to 20, Inclusive)
n = 12

in_range = 10 <= n & n <= 20
print(in_range)

# Exercise 5.  Creating a Boolean Expression for VIP Client Status:
# A costumer is VIP if they have points >= 1000
# (or a partner and have points >= 500)

points = 600
is_partner = True

is_vip = points >= 1000 or (is_partner and points >= 500)

print(is_vip)

# Exercise 6: Implementing Nested Conditionals for Grade Evaluation
# Objective:

# To practice implementing nested conditional statements with logical
# operators to classify numerical grades into specific categories
# ("Excellent", "Aprobado", "Reprobado").

# Task:
#
# Given a numerical grade (nota), write code that applies the following
# classification rules:
#
# If nota is greater than 9, the grade is "Excellent".
# If nota is greater than or equal to 5 AND nota is less than or equal to 9,
# the grade is "Aprobado".
# In all other cases, the grade is "Reprobado".

note = 9.21

if note >= 9:
    print("Well job nerd")
elif note >= 5 and note <= 10:
    print("It´s ok budy")
else:
    print("You failed, try the next bro")


# Exercise 7: Login Authentication with Blocking and OTP
# Objective:
#
# To practice implementing complex conditional logic using boolean variables
# (True/False),
# the not operator, and logical operators (and, or) to determine
# if a user can log in based on multiple criteria,
# including account activation, blocking status,
# password verification, and OTP validation.
#
# Task:
#
# Given the following boolean variables:
#
# cuenta_activa (account active)
# bloqueado (blocked)
# contraseña_correcta (password correct)
# ha_validado_con_OTP (validated with OTP)
# Write a boolean expression that evaluates to True,
# if a user can log in under the following conditions:
#
# Their account is active (cuenta_activa is True).
# They are not blocked (bloqueado is False).
# AND either their password is correct (contraseña_correcta is True)
# OR they have validated with OTP (ha_validado_con_OTP is True).

active_account = True
blocked = False
password_correct = False
validate_otp = True

if active_account and (not blocked) and (password_correct or validate_otp):
    print("Acceso concedido bandido")
else:
    print("Estás denegado pringao")
