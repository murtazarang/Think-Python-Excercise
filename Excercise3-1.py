def right_justify(s):
    n = len(s); #length of s string to be used for calculating the shift in print command below
    print ((70-n) * ' ' + s);

right_justify('hello')