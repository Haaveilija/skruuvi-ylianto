#ifndef MAA_H
#define MAA_H
#include <string>
#include <vector>

class Maa {
    public:
        Maa();
        Maa(std::string maa);
        Maa(int maa, std::vector<std::string> maat);

        std::string shortname();
        std::string longname();
    private:
        std:: string maa;
};
#endif