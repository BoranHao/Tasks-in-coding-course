#include <algorithm>
#include <cmath>
#include <ctime>
#include <fstream>
#include <iostream>
#include <set>
#include <sstream>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <vector>

typedef std::unordered_map<unsigned int, std::vector<std::string>> MySizeMap;
typedef std::array<unsigned int, 26> Counter;

MySizeMap wordsizemap;
MySizeMap wordsizemap1;
MySizeMap wordsizemap2;

typedef std::unordered_map<std::string, std::vector<std::string>> MyLetMap;

MyLetMap wordletmap;
MyLetMap wordletmap1;
MyLetMap wordletmap2;

std::vector<std::string> get_words_from_combs(std::string s, int N) {
  std::vector<std::string> results;
  int i, n;

  std::string c(N, ' ');

  std::sort(begin(s), end(s));
  std::unordered_set<std::string> thecombs;

  std::vector<int> v(s.size(), 0);
  fill(v.begin(), v.begin() + N, 1);
  do {
    n = 0;
    for (i = 0; i < v.size(); i++)
      if (v[i])
        c[n++] = s[i];

    if (thecombs.find(c) != thecombs.end())
      continue;
    thecombs.insert(c);

    auto it = wordletmap.find(c);
    if (it != wordletmap.end())
      for (auto w : wordletmap.at(c)) results.push_back(w);
  } while (prev_permutation(begin(v), end(v)));
  return results;
}

std::vector<std::string> get_words_from_words(std::string s, int N) {
  std::vector<std::string> results;

  Counter sc, wc;
  int i, j;

  for (i = 0; i < 26; i++) sc[i] = 0;
  for (j = 0; j < s.size(); j++) sc[s[j] - 'a']++;

  bool good;

  for (auto w : wordsizemap.at(N)) {
    for (i = 0 ; i < 26 ; i++) wc[i] = 0;
    for (j = 0 ; j < w.size() ; j++) wc[w[j] - 'a']++;

    good = true;
    for (j = 0 ; j < 26 ; j++)
      if (wc[j] > sc[j]) {
        good = false;
        break;
      }

    if (good) {
      results.push_back(w);
    }
  }

  return results;
}

double factorial(int v) {
  return sqrt((2.0 * v + 0.33) * 3.14) * exp(v * log(v) - v);
}

double combinations(int n, int k) {
  if (n == k) return 1;
  return factorial(n) / factorial(n - k) / factorial(k);
}

std::vector<std::string> finnd(std::string theletters, std::string S) {
  int N = S.length();
  std::vector<std::string> fi;
  if (7 * combinations(theletters.size(), N) < wordsizemap[N].size())
    fi = get_words_from_combs(theletters, N);
  else
    fi = get_words_from_words(theletters, N);
  std::string yan = "";
  std::string x = "*";
  for (int i = 0; i < N; ++i)
    yan = yan + x;
  if (yan != S) {
    std::vector<int> ind;
    for (int i = 0; i < N; ++i) {
      if (yan[i] != S[i])
        ind.push_back(i);
    }
    std::vector<std::string>tep;
    for (auto & word : fi) {
      int fla = 1;
      for (auto & ix : ind) {
        if (word[ix] != S[ix]) {
          fla = 0;
          break;
        }
      }
      if (fla == 1)
        tep.push_back(word);
    }
    fi = tep;
  }
  return fi;
}

/////////////////    find letter path  //////////////
class Letter;

typedef std::vector<std::vector<std::string> >matrix;
typedef std::vector<int>cordi;
std::vector<Letter>LL;

class Letter {
 public:
  matrix mat;
  cordi cor;
  std::string lett;
  std::string word;
  std::vector<Letter>subletter;
  int level;
  std::vector<Letter> backletter;
  Letter(matrix, cordi, std::string, std::string,
         std::vector<Letter>, int, std::vector<Letter>);
};


Letter::Letter(matrix n, cordi a, std::string b, std::string c,
               std::vector<Letter>d, int e = 0, std::vector<Letter> f = LL) {
  mat = n;
  cor = a;
  lett = b;
  word = c;
  subletter = d;
  level = e;
  backletter = f;
}


int rowNum[] = {-1, -1, -1, 0, 0, 1, 1, 1};
int colNum[] = {-1, 0, 1, -1, 1, -1, 0, 1};

std::vector<Letter> findnab(Letter letter) {
  std::vector<Letter>suble;
  cordi tu(2);
  tu = letter.cor;
  std::vector<Letter> orr;
  orr.push_back(letter);
  matrix cc = letter.mat;
  int rg = cc.size() - 1;
  for (int k = 0; k < 8; ++k) {
    int tt1 = tu[0] + rowNum[k];
    int tt2 = tu[1] + colNum[k];
    std::string tt;
    tt = letter.word[letter.level + 1];
    if ((tt1 >= 0) && (tt2 >= 0)
        && (tt1 <= rg) && (tt2 <= rg)) {
      if (cc[tt1][tt2] == tt) {
        cordi t1(2);
        std::vector<Letter> L;
        t1[0] = tt1;
        t1[1] = tt2;
        cc[tu[0]][tu[1]] = "";
        Letter am(cc, t1, cc[tt1][tt2],
                  letter.word, L, letter.level + 1, orr);
        suble.push_back(am);
      }
    }
  }
  return suble;
}

std::vector<Letter> lettoblist(matrix mat, std::string word) {
  std::vector<Letter> fii;
  int size = mat.size();
  for (int i = 0; i < size; ++i) {
    for (int j = 0; j < size; ++j) {
      std::string oo;
      oo = word[0];
      if (mat[i][j] == oo) {
        std::vector<int> tu(2);
        tu[0] = i;
        tu[1] = j;
        std::vector<Letter> L;
        Letter s(mat, tu, mat[i][j], word, L, 0, LL);
        fii.push_back(s);
      }
    }
  }
  return fii;
}


void setallsuble(Letter *obb, int times) {
  if ((*obb).subletter.size() != 0) {
    for (auto & letter : (*obb).subletter) {
      if (letter.level != times - 1) {
        letter.subletter = findnab(letter);
        setallsuble(&letter, times);
      }
    }
  }
}


std::vector<std::vector<std::string>>
settt(std::vector<std::vector<std::string>> fi) {
  std::vector<std::vector<std::string>> re;
  int flag = 0;
  for (auto & i : fi) {
    for (auto & j : re) {
      if (i == j) {
        flag = 1;
        break;
      }
    }
    if (flag == 0)
      re.push_back(i);
    flag = 0;
  }
  return re;
}


std::vector<std::vector<std::vector<int>>> ree;

void search(Letter *obb, int times) {
  for (auto & ob : (*obb).subletter) {
    if (ob.level == times - 1) {
      std::vector<std::vector<int>> lsc;
      lsc.insert(lsc.begin(), ob.cor);
      Letter tp = ob.backletter[0];
      for (int i = 0; i < times - 1; ++i) {
        lsc.insert(lsc.begin(), tp.cor);
        if (tp.backletter.size() != 0)
          tp = tp.backletter[0];
      }
      ree.push_back(lsc);
    } else {
      search(&ob, times);
    }
  }
}


std::vector<std::vector<std::vector<int>>>
findpath(matrix mat, std::string target) {
  std::vector<Letter> fii = lettoblist(mat, target);
  std::vector<int> icor;
  Letter ori(mat, icor, "", target, fii);
  setallsuble(&ori, target.length());
  search(&ori, target.length());
  std::vector<std::vector<std::vector<int>>> re;
  re = ree;
  std::vector<std::vector<std::vector<int>>>().swap(ree);
  return re;
}

/////////////     search word path ///////////////
class Path;
std::vector<Path> PP;

std::string staa(matrix mat) {
  std::string lets = "";
  int jie = mat.size();
  for (int i = 0; i < jie; ++i) {
    for (int j = 0; j < jie; ++j) {
      lets.append(mat[i][j], 0, 1);
    }
  }
  return lets;
}


class Path {
 public:
  matrix mat;
  std::string word;
  std::vector<std::vector<int>> cord;
  std::vector<std::string> shapee;
  int level;
  std::vector<Path> backpath;
  std::vector<Path> subpath;
  std::string letters;
  Path(matrix, std::string, std::vector<std::vector<int>>,
       std::vector<std::string>, int, std::vector<Path>);
};

Path::Path(matrix n, std::string a, std::vector<std::vector<int>> b,
           std::vector<std::string> c, int d = 0, std::vector<Path> e = PP) {
  mat = n;
  word = a;
  cord = b;
  shapee = c;
  level = d;
  backpath = e;
  int jie = n.size();
  std::string letts = staa(n);
  letters = letts;
  subpath = PP;
}


matrix down(matrix &mat) {
  int jie = mat.size();
  int fl = 0;
  for (int i = 0; i < jie - 1; ++i) {
    for (int j = 0; j < jie; ++j) {
      if ((mat[i][j] != "") && (mat[i + 1][j] == "")) {
        mat[i + 1][j] = mat[i][j];
        mat[i][j] = "";
        fl = 1;
      }
    }
  }
  if (fl != 0)
    down(mat);
  return mat;
}

matrix removeletter(matrix matt, std::vector<std::vector<int>> cor) {
  matrix mat = matt;
  for (auto & tu : cor) {
    mat[tu[0]][tu[1]] = "";
  }
  return mat;
}

std::vector<Path> findsub(Path obb) {
  matrix tpp = removeletter(obb.mat, obb.cord);
  matrix mxt = down(tpp);
  std::string stmxt = staa(mxt);
  std::vector<Path> rst;
  std::vector<std::string> worlist = finnd(stmxt, obb.shapee[obb.level]);
  std::vector<Path> bob;
  bob.push_back(obb);
  for (auto & word : worlist) {
    std::vector<std::vector<std::vector<int>>> ppaths = findpath(mxt, word);
    if (ppaths.size() != 0) {
      for (auto & ppath : ppaths) {
        Path ob(mxt, word, ppath, obb.shapee, obb.level + 1, bob);
        rst.push_back(ob);
      }
    }
  }
  return rst;
}

void setallsub(Path &obb, int shapee) {
  if (obb.subpath.size() != 0) {
    for (auto & ob : obb.subpath) {
      if (ob.level != shapee) {
        ob.subpath = findsub(ob);
        setallsub(ob, shapee);
      }
    }
  }
}

std::vector<std::vector<std::string>> fina;
void printye(Path obb) {
  for (auto & ob : obb.subpath) {
    if (ob.level == obb.shapee.size()) {
      std::vector<std::string>tp;
      tp.push_back(ob.word);
      Path aa = ob.backpath[0];
      for (int i = 0; i < obb.shapee.size() - 1; ++i) {
        tp.insert(tp.begin(), aa.word);
        aa = aa.backpath[0];
      }
      fina.push_back(tp);
    } else {
      printye(ob);
    }
  }
}


std::vector<std::vector<std::string>>
proc(matrix mm, std::vector<std::string>shape) {
  std::vector<std::vector<int>> nu;
  Path oob(mm, "ori", nu, shape, 0);
  oob.subpath = findsub(oob);
  setallsub(oob, shape.size());
  printye(oob);
  std::vector<std::vector<std::string>> fee = settt(fina);
  std::vector<std::vector<std::string>>().swap(fina);
  return fee;
}

int main(int argc, char const *argv[]) {
  std::ifstream wordfile1(argv[1]);
  std::string w1;

  while (wordfile1 >> w1) {
    wordsizemap1[w1.size()].push_back(w1);
    std::string c1 = w1;
    sort(begin(c1), end(c1));
    wordletmap1[c1].push_back(w1);
  }
  wordfile1.close();
  std::ifstream wordfile2(argv[2]);
  std::string w2;
  while (wordfile2 >> w2) {
    wordsizemap2[w2.size()].push_back(w2);
    std::string c2 = w2;
    sort(begin(c2), end(c2));
    wordletmap2[c2].push_back(w2);
  }
  wordfile2.close();


///////////////   main input begin   ////////////
  std::string line;
  while (std::cin) {
    getline(std::cin, line);
    if (line == "") {
      break;
    }
    std::vector<std::string> puzzle_input;
    int m = line.length();
    for (int i = 0; i < m; ++i) {
      puzzle_input.push_back(line);
      getline(std::cin, line);
    }
    std::vector<std::vector<std::string> >
    puzzle_mat(m, std::vector<std::string>(m, ""));
    for (int j = 0; j < m; ++j) {
      for (int k = 0; k < m; ++k) {
        puzzle_mat[j][k].push_back(puzzle_input[j][k]);
      }
    }
    std::vector<std::string> puzzle_target;
    std::istringstream iss(line);

    for (std::string s; iss >> s; )
      puzzle_target.push_back(s);

    wordsizemap = wordsizemap1;
    wordletmap = wordletmap1;
    std::vector<std::vector<std::string>>
                                       rtt = proc(puzzle_mat, puzzle_target);
    if (rtt.size() == 0) {
      wordsizemap = wordsizemap2;
      wordletmap = wordletmap2;
      rtt = proc(puzzle_mat, puzzle_target);
    }

    for (auto & stset : rtt) {
      std::sort(rtt.begin(), rtt.end());
      for (int i = 0; i < stset.size() - 1; ++i) {
        std::cout << stset[i] << " ";
      }
      std::cout << stset[stset.size() - 1] << std::endl;
    }
    std::cout << "." << std::endl;
  }
  return 0;
}
