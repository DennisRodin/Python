#This is my testing playground of me testing some string functions.


base_text    = "----ThIs TeXt FrAgMeNt WaS nOt EdItEd.---- " 

uppered_text = "----This text fragment was uppered via a code. ----" 

lowered_text = "----This text fragment was lowered via a code. ----" 

strip_text   = "----This text contains eight hyphens.----" 





print(str(base_text + uppered_text.upper() + lowered_text.lower() + strip_text.strip("-") ))