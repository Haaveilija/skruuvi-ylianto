#include "StrUtils.hh"
#include <string>
#include <vector>
#include <iostream>

std::vector<std::string> splits(std::string s, char delimiter) {
    std::string current_word;
    std::vector<std::string> words;
    for (int i = 0; i < s.size(); i++) {
        if (s[i] != delimiter) {
            current_word += s[i];
        } else {
            words.push_back(current_word);
            current_word = "";
        }
    }
    if (s[-1] != delimiter) {
        words.push_back(current_word);
    }
    return words;
}

void print(std::string s)
{
    std::cout << s << std::endl;
}
