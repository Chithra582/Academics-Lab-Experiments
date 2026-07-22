#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct table {
    char var[10];
    int value;
};

struct table tb[21];
int n = 0;

void create();
void insert();
void modify();
int search(char variable[], int n);
void display();

int main()
{
    int ch, result;
    char v[10];
    do
    {
        printf("\n======SYMBOL TABLE MENU=====\n");
        printf("1.Create\n");
        printf("2.Insert\n");
        printf("3.Modify\n");
        printf("4.Search\n");
        printf("5.Display\n");
        printf("6.Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &ch);

        switch(ch)
        {
            case 1:
                create();
                break;
            case 2:
                insert();
                break;
            case 3:
                modify();
                break;
            case 4:
                printf("Enter variable to search: ");
                scanf("%9s", v);
                result = search(v, n);
                if(result == 0)
                {
                    printf("Variable does not exist in the table.\n");
                }
                else
                {
                    printf("Location: %d\n", result);
                    printf("Variable: %s\n", tb[result].var);
                    printf("Value: %d\n", tb[result].value);
                }
                break;
            case 5:
                display();
                break;
            case 6:
                printf("Exiting...\n");
                break;
            default:
                printf("Invalid choice!\n");
        }

    } while(ch != 6);
    return 0;
}

void create(){
    int i, j;
    printf("Enter number of entries: ");
    scanf("%d", &n);
    if (n > 20) {
        printf("Maximum 20 entries allowed.\n");
        n = 20;
    }
    for(i = 1; i <= n; i++){
        while(1)
        {
            printf("Enter variable and value: ");
            scanf("%9s%d", tb[i].var, &tb[i].value);
            if(tb[i].var[0] >= '0' && tb[i].var[0] <= '9'){
                printf("Variable must start with an alphabet.\n");
                continue;
            }
            int duplicate = 0;
            for(j = 1; j < i; j++){
                if(strcmp(tb[i].var, tb[j].var) == 0){
                    duplicate = 1;
                    break;
                }
            }
            if(duplicate){
                printf("Variable already exists. Enter another.\n");
                continue;
            }
            break;
        }
    }
    printf("\nTable Created Successfully\n");
    display();
}

void insert(){
    int j;
    if(n >= 20){
        printf("Table is full.\n");
        return;
    }
    n++;
    while(1){
        printf("Enter variable and value: ");
        scanf("%9s%d", tb[n].var, &tb[n].value);
        if(tb[n].var[0] >= '0' && tb[n].var[0] <= '9'){
            printf("Variable must start with an alphabet.\n");
            continue;
        }
        int duplicate = 0;
        for(j = 1; j < n; j++){
            if(strcmp(tb[n].var, tb[j].var) == 0){
                duplicate = 1;
                break;
            }
        }
        if(duplicate){
            printf("Variable already exists. Enter another.\n");
            continue;
        }
        break;
    }
    printf("\nTable After Insertion\n");
    display();
}

void modify(){
    char variable[10];
    int result;
    printf("Enter variable to modify: ");
    scanf("%9s", variable);
    result = search(variable, n);
    if(result == 0){
        printf("Variable not found.\n");
        return;
    }
    printf("Current value of %s = %d\n", tb[result].var, tb[result].value);
    while(1){
        printf("Enter new variable name and value: ");
        scanf("%9s%d", tb[result].var, &tb[result].value);
        if(tb[result].var[0] >= '0' && tb[result].var[0] <= '9'){
            printf("Variable must start with an alphabet.\n");
            continue;
        }
        break;
    }
    printf("\nTable After Modification\n");
    display();
}

int search(char variable[], int n){
    int i;
    for(i = 1; i <= n; i++){
        if(strcmp(tb[i].var, variable) == 0){
            return i;
        }
    }
    return 0;
}

void display(){
    int i;
    printf("VARIABLE\tVALUE\n");
    for(i = 1; i <= n; i++){
        printf("%s\t%d\n", tb[i].var, tb[i].value);
    }
}
