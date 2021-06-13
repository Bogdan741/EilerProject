/*The cube, 41063625 (3453), can be permuted to produce two other cubes: 56623104
(3843) and 66430125 (4053). In fact, 41063625 is the smallest cube which has exactly
 three permutations of its digits which are also cube.
Find the smallest cube for which exactly five permutations of its digits are cube.*/

#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#include <cmath>
#include <algorithm>

using namespace std;

vector<string> FindNextPermutations(const string &);
string FindTheNumber(int)
bool IsCube(const string & )

int main(){


    return 0;
}

string FindTheNumber(int n)
{
    int i{1};
    while(true){
        int total{};

        stringstream ss;
        ss << i;
        auto t_array = FindNextPermutations(ss.str());
        for(auto & it: t_array)
        {
            if(isCube(it))
                ++total;
        }
        if(total == n)
            return i;
        ++i;
    }
}

bool IsCube(const string & )
{
    unsighed long val{};
    srringstream ss;
    ss >> val;
    int a = floor(pow(val, 1.0/3.0));
    if(fabs(a*a*a - val)<1E-10)
        return true;
    return false;
}

vector<string> FindNextPermutations(const string & val)
{
    vector<string> ar{};
    string valt = val;
    while(true)
    {
        string strt{valt};
        int j=-1;
        for(int i = 0; i < valt.size() - 1; i++)
        {
            char a_j = valt[i];
            char a_jp1 = valt[i+1];
            if(aj < a_jp1)
            {
                bool inc = true;
                for(int t = i+2; t < valt.size();t++)
                {
                    char next = a_jp1;
                    if(next < valt[t])
                    {
                        inc = false;
                        break;
                    }
                    else
                        next = valt[t];
                }
                if(inc)
                {
                    j = i;
                    break;
                }
            }
        }
        if(j == -1)
            break;

        for(int t = valt.size() - 1; t=>0; t--)
        {
            if(valt[t] > valt[j])
            {
                swap(strt[j],strt[k]);
                sort(strt.begin()+j+1,strt.end());
            }
        }
        ar.push_back(strt);
        valt = strt;
    }
    return ar;
}
