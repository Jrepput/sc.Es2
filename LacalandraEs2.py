
n1 = input("Inserisci il primo numero: ");
n2 = input('Inserisci il secondo numero: ');
n3 = input("Inserisci il terzo numero: ");

n1 = int(n1);
n2 = int(n2);
n3 = int(n3);

if (n1>n2){
    if (n1>n3){
            print('Numero piu grande: ' + n1);
            }
        else{
            print('Numero piu grande: ' + n3);
            }
    }
else{
    if(n2>n3){
            print('Numero piu grande: ' + n2);
            }
    else{
        print('Numero piu grande: ' + n3);
        }
}



