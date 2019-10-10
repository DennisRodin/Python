
"""This is my testing playground of me 
   testing some basic string functions."""


base_text    = "----ThIs TeXt FrAgMeNt WaS nOt EdItEd.---- " 

uppered_text = "----This text fragment was uppered via a code. ----" 

lowered_text = "----This text fragment was lowered via a code. ----" 

strip_text   = "----This text contains eight hyphens. ----" 

replaced_text= "----In this text all the 'T' have been replaced with the 'X'. ----"

capitalized_t= "---- This text just got a capitalized 'T'. ---- "



print(str(base_text + uppered_text.upper() + lowered_text.lower() + strip_text.strip("-") + replaced_text.replace("t", "x") + capitalized_t.capitalize() ))