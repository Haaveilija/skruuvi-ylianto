#include "Kortti.hh"
#include "Maa.hh"
#include "Numero.hh"
#include <iostream>
#include "StrUtils.hh"

int main() {
    Maa *m = new Maa("Hertta <3");
    Numero *n = new Numero(2);
    Kortti *k = new Kortti(*n, *m);
    std::string input;

    print("Anna yliantokortit <p|r|R|H><1-14>");
    while (true) {
        std::cin >> input;
        if (input == "q") {
            print("Bye!");
            return EXIT_SUCCESS;
        }

        std::vector<std::string> words = splits(input);

        for (int i = 0; i < words.size();i++) {
            std::string maastr = ""+words[i][0];
            m = new Maa(maastr);
            int num = std::stoi(words[i].substr(1, words[i].size()));
            n = new Numero(num);
            k = new Kortti(*n, *m);
            print(k->longname());
            print("sana oli: "+words[i]);
        }
    }


    

}