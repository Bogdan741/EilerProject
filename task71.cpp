//Brute force actually, solution without it require some number theory see Farey sequences //https://www.xarg.org/puzzle/project-euler/problem-71/
// https://www.xarg.org/puzzle/project-euler/problem-71/


/*Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that 2/5 is the fraction immediately to the left of 3/7.

By listing the set of reduced proper fractions for d ≤ 1,000,000 in ascending order of size, find the
numerator of the fraction immediately to the left of 3/7.*/

#include <iostream>
#include <set>
#include <cmath>
#include <algorithm>
using namespace std;

class Fraction{
    // notice, actually Fraction may be negative(e.g. - 1/7)
    //that is not what is needed in the task, exept in way to compare two fractions
    //but the problem can be solved in other way
private:
    std::size_t num;
    std::size_t denum;
public:
    std::size_t gcd(std::size_t a, std::size_t b)
    {
        if (a == 1 || b == 1)
            return 1;
        else if (a == b)
            return a;
        else
            return gcd(max(a,b) - min(a,b), min(a,b));
    }
    Fraction() = default;
    Fraction(std::size_t n, std::size_t d) : num{n/gcd(n,d)}, denum{d/gcd(n,d)}{}
    std::size_t getDenum() const{return denum;}
    std::size_t getNum() const{return num;}
};
bool operator<(const Fraction & a, const Fraction & b)
{
    return static_cast<double>(a.getNum())/a.getDenum() < static_cast<double>(b.getNum())/b.getDenum();
}
ostream & operator<<(ostream & os, const Fraction & a)
{
    os << "Numerator: " << a.getNum() << endl;
    os << "Denumerator: " << a.getDenum() << endl;
    return os;
}

int main(){
    const int max_den = 1000;
    set<Fraction> list_frac{}; // store elements in order, does not allow duplicates
    //(actually that is strongly simplify the task, and does not reduce efficency, since set is binary tree)
    // that is what we need for the task.
    for(size_t i = 2; i <= max_den; i++)
    {
        for(size_t j = 1; j < i; j++)
        {
            list_frac.insert(Fraction{j, i});
        }
    }
    cout << *list_frac.upper_bound(Fraction{3,7}); // task 71
    cout << list_frac.size();// task 72
    return 0;
}
