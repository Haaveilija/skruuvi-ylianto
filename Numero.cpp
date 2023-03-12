#include "Numero.hh"

Numero::Numero(int n) {
    this->n = n;
}

Numero::Numero() {
    this->n = 1;
}

std::string Numero::numname() {
    const std::map<int, std::string> kuvakortit = {
        {1, "A"},
        {10, "T"},
        {11, "J"},
        {12, "Q"},
        {13, "K"},
        {14, "A"}
    };
    
    if (kuvakortit.find(this->n) != kuvakortit.end()) {
        return std::string(""+kuvakortit.at(this->n));
    } else if (this-> n > 0 && this->n < 10) {
        return std::to_string(this->n);
    } else {
        return "?";
    }
}