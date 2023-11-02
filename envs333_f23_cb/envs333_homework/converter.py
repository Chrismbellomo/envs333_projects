def dd(latdegree, latminute, latsecond, latdirection, londegree, lonminute, lonsecond, londirection):
    # Convert direction values to numerical values or "multipliers"
    lat_direction_multiplier = 1 if latdirection == 'N' else -1
    lon_direction_multiplier = 1 if londirection == 'E' else -1
    
    latdd = lat_direction_multiplier * (latdegree + (latminute + latsecond/60.)/60.)
    londd = lon_direction_multiplier * (londegree + (lonminute + lonsecond/60.)/60.)
    
    return latdd, londd

#This is a function that takes a user input DNA sequence and converts it to RNA
def dna_to_rna(dna_sequence):
    rna_sequence = dna_sequence.replace("T", "U")
    return rna_sequence


#This is a function that takes a user input RNA sequence and converts it to DNA
def rna_to_dna(rna_sequence):
    dna_sequence = rna_sequence.replace("U", "T")
    return dna_sequence

#This is a microliter to mililiter converter
def ul_to_ml(ul):
    ml = ul / 1000
    return ml

#this is a mililiter to microliter converter
def ml_to_ul(ml):
    ul = ml * 1000
    return ul

#This function converts miles to feet
def miles_to_feet(miles):
    feet = miles * 5280
    return feet

#This function converts feet to miles
def feet_to_miles(feet):
    miles = feet/5280
    return miles