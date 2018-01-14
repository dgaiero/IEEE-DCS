# Verification of PolyCard and Extraction of Useful PolyCard Data
# Author: Russell Caletena
# Date Created: 12/16/17

'''
Sample PolyCard data
***REMOVED***
'''

# Valid PolyCard Data
x = '***REMOVED***'

# Invalid PolyCard Data
#x = 'ajkslfjlaskjfklasjklfjaskljflsakjf'

def separate_ISO_And_Lib_Number(polyCardData):
    while True:
        # Verifies if card swiped is a PolyCard
        if (len(polyCardData)   == 41        and
            polyCardData[0]     == '%'       and
            polyCardData[14]    == '^'       and
            polyCardData[15:22] == 'STUDENT' and
            polyCardData[22]    == '?'       and
            polyCardData[23]    == ';'       and
            polyCardData[40]    == '?'):

            # Extracts useful info from PolyCard and stores in a dictionary
            library_Code_Number = int(polyCardData[1:14])
            iso_Number = int(polyCardData[24:40])
            useful_polyCard_Data = {'libraryCodeNumber': library_Code_Number,
                                    'isoNumber'        : iso_Number,
            }
            return useful_polyCard_Data

        else:
            # Returns 'None' if card is invalid
            print ('Invalid card! Please try again.')
            break

y = separate_ISO_And_Lib_Number(x)
print (y)
