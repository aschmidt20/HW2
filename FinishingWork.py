#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <string>
#include <queue>
#include <utility>
#include <sstream>

using namespace std;

pair<long, long> parse_line(string line)
{
    // Turns each line into a pair
    long n1, n2;
    stringstream ss;
    ss << line;
    ss >> n1; 
    ss >> n2; 
    return make_pair(n1, n2);
}

long parse_pair(pair<long, long> arg, long begin)
{
    // Adds the pair to the running total
    return begin + arg.first - arg.second;
}


int main() {
    // Get number of cases and build line 
    // NASTY way to do it 
    long num_cases;
    string line; 
    getline(cin, line);
    stringstream ss; 
    ss << line;
    ss >> num_cases;
    
    // Builds vector of cases 
    vector<pair<long, long>> cases;
    while (getline(cin, line))
    {
        cases.push_back(parse_line(line));
    }
    
    // Loop over every line
    for (size_t i = 0; i != cases.size(); ++i)
    {
        long begin = 0;
        size_t j = 0;
        
        // Loop over every line 
        while (begin >= 0 && j != cases.size())
        {
            // Parse the line at the i + jth position
            begin = parse_pair(cases.at((i + j) % cases.size()), begin);
            j++;
        }
        
        // Only if we hit the end
        if (j == cases.size())
        {
            cout << i;
        }
    }
    
    
    
    

    
    
}
