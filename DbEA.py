"""
    MamadouLAMINESENE
    ML__SENE___17
"""
class DbEA:
    def __init__(self):
        pass
    """
        Function pour avoir toutes les region
        et leur department
    """
    def getDict(self):
        region,departement=4,5
        donne={}
        for key,val in region.items():
            donne[key]=[]
            for keyFils,valFils in departement.items():
                if val==valFils:
                    donne[key].append(keyFils)
        return donne