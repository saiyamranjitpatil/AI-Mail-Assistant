import math

def estimate_reading_time(text):

    """

    Estimates email reading time based on

    an average reading speed of 200 words/minute.

    """

    if not text:

        return "Less than 1 min"



    words = len(text.split())



    minutes = math.ceil(words / 200)



    if minutes <= 1:

        return "Less than 1 min"



    return f"{minutes} mins"