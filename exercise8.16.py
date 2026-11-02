# 1. Import seluruh module
import greeting
greeting.greet('Yusrina')

# 2. Import function tertentu
from greeting import greet
greet('Domi')

# 3. Import function dengan alias
from greeting import greet as g
g('Ael')

# 4. Import module dengan alias
import greeting as gr
gr.greet('Nissa')

# 5. Import semua function
from greeting import *
greet('Nayla')