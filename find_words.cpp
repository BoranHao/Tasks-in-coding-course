#include <algorithm>
#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <unordered_map>
#include <vector>

using std::string;
using std::vector;
using std::unordered_map;
using std::ifstream;
using std::cout;
using std::endl;
using std::cin;
using std::istringstream;

typedef unordered_map<string, int> stadict;
typedef unordered_map<string, stadict> worddict;
typedef unordered_map<string, worddict> inidict;
typedef unordered_map<int, inidict> oridict;

typedef vector<int> intvector;
typedef vector<vector<int>> helvec;

string com(string word);
stadict sta(string wrd);
int min(int a, int b);
helvec combine(int n, int k);


int main(int len, char* argv[]) {
  oridict staaa;

  string filename = argv[1];


  ifstream in(filename);
  string line;

  if (in) {
    while (getline(in, line)) {
      staaa[line.length()][com(line)][line] = sta(line);
    }
  }


  string letter;
  string lo;
  int lon;

  while (true) {
    string inp;
    getline(cin, inp);
    if (inp == "") {
      break;
    }

    istringstream is(inp);
    is >> letter >> lo;
    lon = stoi(lo);
    if (lon == 0) {
      break;
    }

    vector<string>fi;
    string ccc = com(letter);
    stadict tar = sta(letter);

    int ran = min(lon, ccc.length());
    int loo = ccc.length();


    for (int i = 1; i <= ran; i++) {
      helvec re;
      re = combine(loo, i);
      for (auto & e : re) {
        string key_ini = "";
        for (auto & a : e) {
          int aa = a - 1;

          key_ini.append(ccc, aa, 1);
        }

        for (auto key2 : staaa[lon][key_ini]) {
          string key_words = key2.first;
          int flag = 0;
          try {
            for (auto key3 : staaa[lon][key_ini][key_words]) {
              string key_lett = key3.first;
              if (staaa[lon][key_ini][key_words][key_lett] > tar[key_lett]) {
                flag = 1;
                break;
              }
            }
          } catch(...) {
            continue;
          }
          if (flag == 0) {
            fi.push_back(key_words);
          }
        }
      }
    }
    std::sort(fi.begin(), fi.end());
    for (auto& e : fi) {
      cout << e << endl;
    }
    cout << "." << endl;
  }
  return 0;
}

string com(string wrd) {
  string a;
  string tm;
  int lon;
  lon = wrd.length();
  stadict ss;
  for (int i = 0; i < lon; i++) {
    tm = wrd[i];
    ss[tm] = 0;
  }
  for (auto & em : ss) {
    a.append(em.first);
  }
  sort(a.begin(), a.end());
  return (a);
}

stadict sta(string wrd) {
  stadict ss;
  string tm;
  int lon = wrd.length();
  for (int i = 0; i < lon; i++) {
    tm = wrd[i];
    ss[tm] = 0;
  }
  for (int i = 0; i < lon; i++) {
    tm = wrd[i];
    ss[tm]++;
  }
  return ss;
}

int min(int a, int b) {
  int c = a;
  if (a > b) {
    c = b;
  }
  return c;
}

vector<vector<int>> combine(int n, int k) {
  vector<vector<int>> res;
  vector<int> out(k, 0);
  int i = 0;
  while (i >= 0) {
    ++out[i];
    if (out[i] > n) {
      --i;
    } else if (i == k - 1) {
      res.push_back(out);
    } else {
      ++i;
      out[i] = out[i - 1];
    }
  }
  return res;
}
