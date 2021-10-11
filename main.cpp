#include <fstream>
#include <bits/stdc++.h>

using namespace std;
ifstream inFile;
const int lenDatos = 4 ;
/*
void casoI(int actividades[][lenDatos],int ar[]);
void recur(int i, int j, int mat[][4], int n){
    int matsol[24][n];
    int mataux[24][n];
    if(i>mat[i][3]){
        matsol[i][1] = 0;
    }
};*/
int main(){
  inFile.open("/home/jose/valle/sexto/FADA/Proyecto Fada/entrada.txt");
  if(!inFile){
      cerr << "Error al acceder al archivo entrada.txt";
      exit(1);
  }
  int n ;
  inFile >> n;
  string nombre[n];
  int horario[n][3];

  for(int i=0;i<n;i++){
      inFile >> nombre[i];
      inFile >> horario[i][0];
      inFile >> horario[i][1];
      horario[i][2] = horario[i][1] - horario[i][0];
  }
  inFile.close();

    return 0;
}

