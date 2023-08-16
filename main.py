from models.compound_list import *
from models.list_graphics import *
if __name__ == '__main__':

    HBA_compounds = ['PROLINE',
                     'BETAINE',
                     'DGLUCOSE',
                     'GLUCOSE',
                     'FRUCTOSE',
                     'SUCROSE',
                     'MALTOSE',
                     'XYLOSE',
                     'CITRIC_ACID',
                     'LACTIC_ACID',
                     'MALIC_ACID',
                     'L-MENTHOL',
                     'GLYCEROL',
                    ]
    HBD_compounds = ['FORMIC_ACID',
                     'ACETIC_ACID',
                     'OXALIC_ACID',
                     'MALONIC_ACID',
                     'TARTARIC_ACID',
                     'LEVULINIC_ACID',
                     'PROPIONIC_ACID',
                     'N-HEXANOIC_ACID',
                     'N-OCTANOIC_ACID',
                     'N-DECANOIC_ACID',
                     'N-DODECANOIC_ACID',
                     'N-TETRADECANOIC_ACID',
                     'OLEIC_ACID',
                     'RICINOLEIC_ACID',
                     'BENZOIC_ACID',
                     '4-HYDROXY-PHENYLACETIC_ACID',
                     '1-HEXANOL',
                     '1-OCTANOL',
                     '1-DECANOL',
                     '1-DODECANOL',
                     '1-TETRADECANOL',
                     '1-HEXADECANOL',
                     'ETHYLENE_GLYCOL',
                     'TRIETHYLENE_GLYCOL',
                     '1,3-PROPANEDIOL',
                     '1,2-BUTANEDIOL',
                     '1,3-BUTANEDIOL',
                     '1,4-BUTANEDIOL',
                     '1,6-HEXANEDIOL',
                     'CYCLOHEXANOL',
                     'UREA',
                     ]
    x = EquimolarDictComp(selected_model='COSMO-SAC-HB2 (GAMESS)',
                          temperature=298.0,
                          solute='CURCUMINA',
                          HBA_list=HBA_compounds,
                          HBD_list=HBD_compounds)
    y = PredictGraphic(x.equimolar_comp_dict)
    #y.graphic_gen_2()
    z = Worksheet(x.compounds_dict)
    """comp_dict = CompoudDictionary(selected_model='COSMO-SAC-HB2 (GAMESS)',
                                                list_type=2,
                                                comp_0="LIDOCAINE",
                                                temperature=298.0,
                                                n_comp_sol=3)

    """