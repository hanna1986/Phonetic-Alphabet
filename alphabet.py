class Alphabet:

    def covert(name: str, dictionary: dict):
        #from alphabet_dict import Alphabet_dict
        #alpha = Alphabet_dict.alpha

        #name = "Yuriy Indman"
        output=""
        
        for letter in name:
            if letter == " ":
                output = output + "space\n"
            else:
                output = output + dictionary.get(letter) + "\n"

        return output
    
