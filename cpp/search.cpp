#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
using namespace std;

string toLower(const string& str) {
    string lower = str;
    transform(lower.begin(), lower.end(), lower.begin(), ::tolower);
    return lower;
}

int main(int argc, char* argv[]) {
    if (argc < 3) {
        cerr << "Usage: " << argv[0] << " <file> <keyword>\n";
        return 1;
    }

    ifstream file(argv[1]);
    if (!file) {
        cerr << "Error: cannot open file " << argv[1] << endl;
        return 1;
    }

    string keyword = toLower(argv[2]);
    string line;
    int lineNo = 0;

    while (getline(file, line)) {
        lineNo++;
        string lowerLine = toLower(line);
        if (lowerLine.find(keyword) != string::npos) {
            cout << "Line " << lineNo << ": " << line << endl;
        }
    }

    file.close();
    return 0;
}

