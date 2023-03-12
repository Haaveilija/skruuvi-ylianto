#ifndef KORTTI_H
#define KORRTI_H

#include <string>
#include "Maa.hh"
#include "Numero.hh"


class Kortti {
    public:
        Kortti(Numero numero, Maa maa);
        Kortti(int numero, std::string maa);

        std::string shortname();
        std::string longname();

    private:
        Numero numero;
        Maa maa;
};

#endif