"""
    enum: DBMV_Mark
    Special ASCII characters used by Multivalued Databases.

    --- Code
        IM = chr(255)
        AM = chr(254)
        VM = chr(253)
        SM = chr(252)
        TM = chr(251)
    ---
"""
class DBMV_Mark:
    IM = chr(255)
    AM = chr(254)
    VM = chr(253)
    SM = chr(252)
    TM = chr(251)

    IM_str = "\u00FF"
    AM_str = "\u00FE"
    VM_str = "\u00FD"
    SM_str = "\u00FC"
    TM_str = "\u00FB"

    IM_txt = "[@@IM@]"
    AM_txt = "[@@AM@]"
    VM_txt = "[@@VM@]"
    SM_txt = "[@@SM@]"
    TM_txt = "[@@TM@]" 
