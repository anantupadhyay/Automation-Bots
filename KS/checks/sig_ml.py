import talon
# don't forget to init the library first
# it loads machine learning classifiers
talon.init()

from talon import signature


message = """Annette Anderson,
11833 Spring Laurel DR
Charlotte, NC 28215
704-724-4697
 
Client is a referral from our chiro- she is there now about to have her appointment. Please reach out in the next hour!
 
Respectfully,

Lacie N. Johnson
Intake Paralegal 
Law Offices of Shane Smith, PC
263 Hwy 74 N
Peachtree City, GA 30269

770.487.8999 ext. 42
770.631.7667 fax
"""

text, signature = signature.extract(message, sender='john.doe@example.com')
print text
