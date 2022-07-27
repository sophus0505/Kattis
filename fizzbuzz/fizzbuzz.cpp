#include <iostream>

using namespace std;


int fizzbuzz(int x, int y, int N){

    int fizz = 1;
    int buzz = 1; 
    string print = ""; 

    for (size_t i = 1; i < N+1; i++){
        if (i % x == 0){
            print += "Fizz"; 
            fizz = 0; 
        } 
        if (i % y == 0){
            print += "Buzz"; 
            buzz = 0; 
        }
        if (fizz == 1 && buzz == 1){
            cout << i << endl;
        } else{
            cout << print << endl;
            print = "";
        }
        fizz = 1;
        buzz = 1;
    }
    return 0; 
}

int main(int argc, char const *argv[])
{
    int x, y, N;
    cin >> x >> y >> N; 

    fizzbuzz(x, y, N); 
    return 0;

}
