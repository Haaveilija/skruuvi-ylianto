#include "Kortti.hh"
#include "Maa.hh"
#include "Numero.hh"

Kortti::Kortti(Numero numero, Maa maa)
{
    this->numero = numero;
    this->maa = maa;
}

std::string Kortti::shortname()
{
    return "Kortin lyhyt nimi: " + this->maa.shortname() + this->numero.numname();
}

std::string Kortti::longname()
{
    return "Kortin pitka nimi: " + this->maa.longname() + this->numero.numname();
}
