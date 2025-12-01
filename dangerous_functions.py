#TEST FILE 02


import os

# Using eval (B307)
code = "print('Hacked!')"
eval(code)

# Using exec
script = "print('Executing dangerous script')"
exec(script)

# Reading system files
print(os.system("cat /etc/passwd"))
