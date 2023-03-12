#ifndef NUMERO_H
#define NUMERO_H
#include <string>
#include <map>

class Numero {
    public:
        Numero(int n);
        Numero();
        std::string numname();
        int getNum();

    private:
        int n;
};
#endif 