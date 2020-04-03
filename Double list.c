#include <stdio.h>
#include <stdlib.h>

typedef struct doubleList
{
    int data;
    struct doubleList *left;
    struct doubleList *right;
} DouList;
void bubble_sort(int *array, int n);       // ������
void add(DouList *header, int data);       // ��β��Ӻ���
DouList *init_list(int n);                 // ��ʼ��ָ�����ȵı�
void output(DouList *header);              // ��������Ϣ82������and��������������Ƿ�����˫����ѭ����
DouList *set_order_list();                 // ��ָ��Ԫ�ؽ���һ��������
void setify(DouList **header);             // ���ϻ�����
int isInList(DouList *, int);              // �ж�Ԫ���Ƿ���������
void del_value(DouList *header, int data); // ɾ������ָ��Ԫ��

DouList *init_list(int n)
{
    DouList *header = (DouList *)malloc(sizeof(DouList));
    DouList *p = header;
    header->left = header;
    header->right = header;
    for (int i = 0; i < n; i++)
    {
        DouList *newNode = (DouList *)malloc(sizeof(DouList));
        p->right = newNode;
        newNode->data = 0;
        newNode->left = p;
        newNode->right = header;
        p = p->right;
        header->left = newNode;
    }
    header->data = n;
    return header;
}

void add(DouList *header, int data)
{
    DouList *p = (DouList *)malloc(sizeof(DouList));
    p = header->left;
    DouList *newNode = (DouList *)malloc(sizeof(DouList));
    newNode->right = header;
    newNode->left = p;
    p->right = newNode;
    header->left = newNode;
    newNode->data = data;
    header->data++;
}

void output(DouList *header)
{
    printf("The length of double list is %d\n", header->data);
    printf("The data are:\n");
    DouList *p = header->right;
    for (int i = 0; i < header->data * 2 + 1; i++)
    {
        printf("%-3d", p->data);
        p = p->right;
    }
    printf("\n");

    p = p->left;
    for (int i = 0; i < header->data * 2 + 1; i++)
    {
        printf("%-3d", p->data);
        p = p->left;
    }
    printf("\n");
}

DouList *set_order_list()
{
    int array[20] = {0};
    DouList *header = init_list(0);
    printf("Please enter the number of data you want:");
    int n;
    scanf("%d", &n);
    for (int i = 0; i < n; i++)
    {
        scanf("%d", &array[i]);
    }
    buuble_sort(array, n);
    for (int i = 0; i < n; i++)
    {
        add(header, array[i]);
    }
    return header;
}

void del_value(DouList *header, int data)
{
    int flag = 1;
    DouList *p = header;
    while (flag == 1)
    {
        flag = 0;
        for (int i = 0; i < header->data; i++)
        {
            if (p->right->data == data)
            {
                p->right = p->right->right;
                p->right->right->left = p;
                header->data--;
                flag = 1;
            }
            p = p->right;
        }
    }
}



//����Ϊ�ڶ�����������ӵ�����
int isInList(DouList *header, int data)
{
    DouList *p = header->right;
    for (int i = 0; i < header->data; i++)
    {
        if (p->data == data)
            return 1;

        p = p->right;
    }
    return 0;
}

void setify(DouList **header)
{
    DouList *newHeader = init_list(0);
    DouList *p = (*header)->right;
    for (int i = 0; i < (*header)->data; i++)
    {
        if (!isInList(newHeader, p->data))
        {
            add(newHeader, p->data);
        }
        p = p->right;
    }
    *header = newHeader;
}

void bubble_sort(int *array, int n)
{
    int flag = 1;
    while (flag)
    {
        flag = 0;
        for (int i = 0; i < n - 1; i++)
        {
            if (array[i] > array[i + 1])
            {
                int tmp = array[i];
                array[i] = array[i + 1];
                array[i + 1] = tmp;
                flag = 1;
            }
        }
    }
}

void display(int *arr, int size)
{
    for (int i = 0; i < size; i++)
    {
        cout << arr[i] << " ";
    }
    cout << endl;
}

void swap(int &a, int &b)
{
    int temp = a;
    a = b;
    b = temp;
}


int section(int *arr, int size, int pos)
{
    int min_index = pos, flag = 0;
    for (int i = pos + 1; i < size; i++)
    {
        if (arr[i] < arr[min_index])
        {
            min_index = i;
            flag = 1;
        }
    }
    if (flag == 1)
        swap(arr[pos], arr[min_index]);

    return flag;
}
void Selection_sort(int *arr, int size)
{
    for (int i = 0; i < size; i++)
    {
        section(arr, size, i);
    }
}
