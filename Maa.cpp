#include "Maa.hh"
#include <iostream>

Maa::Maa(std::string maa) {
    this->maa = maa;
}

Maa::Maa() {
    this->maa = "Pata";
}

std::string Maa::shortname() {
    std::string shortstr;
    shortstr += this->maa[0];
    return shortstr;
}

std::string Maa::longname()
{
    return this->maa;
}
