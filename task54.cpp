
/*In the card game poker, a hand consists of five cards and are ranked, from lowest to highest, in the following way:

High Card: Highest value card.
One Pair: Two cards of the same value.
Two Pairs: Two different pairs.
Three of a Kind: Three cards of the same value.
Straight: All cards are consecutive values.
Flush: All cards of the same suit.
Full House: Three of a kind and a pair.
Four of a Kind: Four cards of the same value.
Straight Flush: All cards are consecutive values of same suit.
Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

If two players have the same ranked hands then the rank made up of the highest value wins; for example, a pair of eights beats a pair of fives (see example 1 below). But if two ranks tie, for example, both players have a pair of queens, then highest cards in each hand are compared (see example 4 below); if the highest cards tie then the next highest cards are compared, and so on.

Consider the following five hands dealt to two players:

Hand	 	Player 1	 	Player 2	 	Winner
1	 	5H 5C 6S 7S KD
Pair of Fives
 	2C 3S 8S 8D TD
Pair of Eights
 	Player 2
2	 	5D 8C 9S JS AC
Highest card Ace
 	2C 5C 7D 8S QH
Highest card Queen
 	Player 1
3	 	2D 9C AS AH AC
Three Aces
 	3D 6D 7D TD QD
Flush with Diamonds
 	Player 2
4	 	4D 6S 9H QH QC
Pair of Queens
Highest card Nine
 	3D 6D 7H QD QS
Pair of Queens
Highest card Seven
 	Player 1
5	 	2H 2D 4C 4D 4S
Full House
With Three Fours
 	3C 3D 3S 9S 9D
Full House
with Three Threes
 	Player 1
The file, poker.txt, contains one-thousand random hands dealt to two players. Each line of the file contains ten cards (separated by a single space): the first five are Player 1's cards and the last five are Player 2's cards. You can assume that all hands are valid (no invalid characters or repeated cards), each player's hand is in no specific order, and in each hand there is a clear winner.

How many hands does Player 1 win?*/
#include <iostream>
#include <array>
#include <chrono>
#include <map>
#include <unordered_map>
#include <utility>
#include <functional>
#include <fstream>
#include <initializer_list>
#include <string>
#include <sstream>


using namespace std;
using namespace chrono_literals;
using Iter = array<pair<int, int>,5>::const_iterator;

const short CARDS_IN_HAND = 5;

//Useful alieses, handle magical numbers(mostly)
enum State{
  WON, LOST, DRAW
};
enum Suit{
  CLUBS, DIAMONDS, HEARTS, SPADES
};
enum Value{
  TWO, THREE, FOUR, FIFE, SIX, SEVEN, EIGHT, NINE, TEN, JACK, QUEEN, KING, ACE
};
struct Player{
  // store data in order according to the key(value in this contest)
  //!!!!!!!!!!!!! VERY IMPORTANT, most of the functions realise on this
  array<pair<int, int>,CARDS_IN_HAND> deck;
};


//----------------------Main function----------------------------------
//Reliases on Player invariant about data

State who_won(const Player &, const Player &);

State HighCard(const Player&, const Player&);
State OnePair(const Player&, const Player&);
State TwoPairs(const Player&, const Player&);
State ThreeOfAKind(const Player&, const Player&);
State Straight(const Player&, const Player&);
State Flush(const Player&, const Player&);
State FullHouse(const Player&, const Player&);
State FourOfAKind(const Player&, const Player&);
State StraightFlush(const Player&, const Player&);
State RoyalFlush(const Player&, const Player&);


//--------------Helper function-----------------------------
Iter findPair(Iter beg, Iter end);
Iter findThree(Iter beg, Iter end);
bool IsSameSuit(Iter beg, Iter end);
bool IsConsecutive(Iter beg, Iter end);
Player Parcer(const string & );

unordered_map<int, function<State(const Player&, const Player&)>> priority{
  {1, RoyalFlush},
  {2, StraightFlush},
  {3, StraightFlush},
  {4, FourOfAKind},
  {5, FullHouse},
  {6, Flush},
  {7, Straight},
  {8, ThreeOfAKind},
  {9, TwoPairs},
  {10, OnePair},
  {11, HighCard},
};

//--------------------------------------------------------------------------------
int main(){
    auto t1 = chrono::steady_clock::now();

  size_t total1{};
  size_t total2{};
  size_t total_draw{};
  ifstream is{ "file54.txt" };
  if (is.is_open())
  {
      while (!is.eof())
      {
          string str;
          getline(is, str);

          Player first = Parcer(string{str.begin(), str.begin() + 15});
          Player second = Parcer(string{ str.begin()+15, str.end() });
          
          bool res = who_won(first, second);

          if (res == State::WON)
              ++total1;
          else if (res == State::LOST)
              ++total2;
          else
              ++total_draw;
      }
  }
  cout <<"The First won: " << total1 <<" times"<<endl;
  auto t2 = chrono::steady_clock::now();
  cout << "The time: " << chrono::duration_cast<chrono::milliseconds>(t2 - t1).count() << endl;

  return 0;
}

Player Parcer(const string& a) {
    array<pair<int, int>, 5> tmp;
    auto beg = tmp.begin();
    stringstream ss;
    ss << a;
    while (!ss.eof() && beg != tmp.end())
    {
        char ch;
        ss >> ch;

        switch (ch)
        {
        case '2': beg->first = Value::TWO; break;
        case '3': beg->first = Value::THREE; break;
        case '4': beg->first = Value::FOUR; break;
        case '5': beg->first = Value::FIFE; break;
        case '6': beg->first = Value::SIX; break;
        case '7': beg->first = Value::SEVEN; break;
        case '8': beg->first = Value::EIGHT; break;
        case '9': beg->first = Value::NINE; break;
        case 'T': beg->first = Value::TEN; break;
        case 'J': beg->first = Value::JACK; break;
        case 'Q': beg->first = Value::QUEEN; break;
        case 'K': beg->first = Value::KING; break;
        case 'A': beg->first = Value::ACE; break;
        case 'D': beg->second = Suit::DIAMONDS; ++beg; break;
        case 'S': beg->second = Suit::SPADES; ++beg; break;
        case 'C': beg->second = Suit::CLUBS; ++beg; break;
        case 'H': beg->second = Suit::HEARTS; ++beg; break;
        }
    }
    sort(tmp.begin(), tmp.end(), [](const pair<int, int>& a, const pair<int, int>& b) {return a.first < b.first; });
    return Player{ tmp };
}
//--------------------------------------------------------------------------------
State who_won(const Player & a, const Player & b)
{
  for(int i = 1; i <= priority.size(); i++)
  {
    auto tmp = priority[i](a, b);
    if(tmp != State::DRAW)
      return tmp;
  }
  return State::DRAW;
}
//--------------------------------------------------------------------------------
State HighCard(const Player& a, const Player& b)
{
  for(int i = CARDS_IN_HAND - 1; i >= 0; i-- )
  {
    if(a.deck[i].first != b.deck[i].first)
        return a.deck[i].first < b.deck[i].first? State::LOST: State::WON;
  }
  return State::DRAW;
}
//--------------------------------------------------------------------------------
Iter findPair(Iter beg, Iter end)
{
    if (end!=beg)
    {
        for (auto i = end - 1; i != beg; --i)
        {
            if ((*i).first == (*(i - 1)).first)
                return i - 1;
        }
    }
    return end;
}
//--------------------------------------------------------------------------------
State OnePair(const Player& a, const Player& b)
{
  int max_pair1 = findPair(a.deck.begin(), a.deck.end()) == a.deck.end()? -1: (*findPair(a.deck.begin(), a.deck.end())).first;
  int max_pair2 = findPair(b.deck.begin(), b.deck.end()) == b.deck.end()? -1: (*findPair(b.deck.begin(), b.deck.end())).first;
  if(max_pair1 != max_pair2)
  {
    return max_pair1 < max_pair2 ? State::LOST : WON;
  }
  return State::DRAW;
}
//--------------------------------------------------------------------------------
State TwoPairs(const Player& a, const Player& b)
{
  Iter max_iter1 = findPair(a.deck.begin(), a.deck.end());
  Iter lover_iter1 = findPair(a.deck.begin(), max_iter1);

  Iter max_iter2 = findPair(b.deck.begin(), b.deck.end());
  Iter lover_iter2 = findPair(b.deck.begin(), max_iter2);

  int max_value1 = max_iter1 == a.deck.end() ? -1: max_iter1->first;
  int value1 =  lover_iter1 == max_iter1 ? -1: lover_iter1->first;

  int max_value2 = max_iter2 == b.deck.end() ? -1: max_iter2->first;
  int value2 =  lover_iter2 == max_iter2 ? -1: lover_iter2->first;

  if(max_value1 != max_value2)
    return max_value1 < max_value2 ? State::LOST : State::WON;
  else
  {
    if(value1 != value2)
      return value1 < value2 ? State::LOST : State::WON;
    else
      return State::DRAW;
  }
}
//--------------------------------------------------------------------------------
Iter findThree(Iter beg, Iter end)
{
    for (auto i = end - 1; i != beg + 1; i--) {
      if((*i).first == (*(i - 1)).first && (*(i - 1)).first == (*(i-2)).first)
        return i-2;
    }
    return end;
}
//--------------------------------------------------------------------------------
State ThreeOfAKind(const Player& a, const Player& b)
{
  int max_three1 = findThree(a.deck.begin(), a.deck.end()) == a.deck.end()? -1: findThree(a.deck.begin(), a.deck.end())->first;
  int max_three2 = findThree(b.deck.begin(), b.deck.end()) == b.deck.end()? -1: findThree(b.deck.begin(), b.deck.end())->first;
  if(max_three1 != max_three2)
  {
    return max_three1 < max_three2 ? State::LOST : WON;
  }
  return State::DRAW;
}
//--------------------------------------------------------------------------------
bool IsConsecutive(Iter beg, Iter end)
{
  for(auto i = beg; i!=end-1; i++)
  {
    if(((*(i+1)).first - (*i).first) != 1)
      return false;
  }
  return true;
}
//--------------------------------------------------------------------------------
State Straight(const Player& a, const Player& b)
{
  bool a_state = IsConsecutive(a.deck.begin(), a.deck.end());
  bool b_state = IsConsecutive(b.deck.begin(), b.deck.end());

  if(a_state && b_state)
    return HighCard(a,b);
  else if(a_state)
    return State::WON;
  else if (b_state)
    return State::LOST;
  else
    return State::DRAW;
}
//--------------------------------------------------------------------------------
bool IsSameSuit(Iter beg, Iter end)
{
  for(auto i = beg; i!=end-1; i++)
  {
    if(((*(i+1)).second != (*i).second))
      return false;
  }
  return true;
}
//--------------------------------------------------------------------------------
State Flush(const Player& a, const Player& b)
{
  bool a_state = IsSameSuit(a.deck.begin(), a.deck.end());
  bool b_state = IsSameSuit(b.deck.begin(), b.deck.end());
  if(a_state && b_state)
    return State::DRAW;
  else if(a_state)
    return State::WON;
  else if (b_state)
    return State::LOST;
  else
    return State::DRAW;
}
//--------------------------------------------------------------------------------
State FullHouse(const Player& a, const Player& b)
{
  Iter three1 = findThree(a.deck.begin(), a.deck.end());
  Iter three2 = findThree(b.deck.begin(), b.deck.end());

  Iter pair1 = findPair(a.deck.begin(), three1);
  Iter pair2 = findPair(b.deck.begin(), three2);

  bool a_state = \
  three1 == a.deck.end()? false : (pair1 == three1 ? false : true);

  bool b_state = \
  three2 == b.deck.end()? false : (pair2 == three2 ? false : true);

  if(a_state && b_state)
    return State::DRAW;
  else if(a_state)
    return State::WON;
  else if (b_state)
    return State::LOST;
  else
    return State::DRAW;
}
//--------------------------------------------------------------------------------
State FourOfAKind(const Player& a, const Player& b)
{
  bool a_state = (a.deck[1] == a.deck[4] || a.deck[0] == a.deck[3]);
  bool b_state = (b.deck[1] == b.deck[4] || b.deck[0] == b.deck[3]);

  if(a_state && b_state)
    return State::DRAW;
  else if(a_state)
    return State::WON;
  else if (b_state)
    return State::LOST;
  else
    return State::DRAW;
}
//--------------------------------------------------------------------------------
State StraightFlush(const Player& a, const Player& b)
{
  bool a_state = IsConsecutive(a.deck.begin(), a.deck.end())\
  && IsSameSuit(a.deck.begin(), a.deck.end());

  bool b_state = IsConsecutive(b.deck.begin(), b.deck.end())\
  && IsSameSuit(b.deck.begin(), b.deck.end());

  if(a_state && b_state)
    return State::DRAW;
  else if(a_state)
    return State::WON;
  else if (b_state)
    return State::LOST;
  else
    return State::DRAW;

}
//--------------------------------------------------------------------------------
State RoyalFlush(const Player& a, const Player& b)
{
  bool a_state = (a.deck[CARDS_IN_HAND - 1].first == Value::ACE) && IsConsecutive(a.deck.begin(), a.deck.end())\
  && IsSameSuit(a.deck.begin(), a.deck.end());

  bool b_state = (b.deck[CARDS_IN_HAND - 1].first == Value::ACE) && IsConsecutive(b.deck.begin(), b.deck.end())\
  && IsSameSuit(b.deck.begin(), b.deck.end());

  if(a_state && b_state)
    return State::DRAW;
  else if(a_state)
    return State::WON;
  else if (b_state)
    return State::LOST;
  else
    return State::DRAW;
}
//--------------------------------------------------------------------------------
