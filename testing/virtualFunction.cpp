#include <stdio.h>

class Base1
{
public:
    virtual int virt1()
    {
        return 100;
    }
    
    int data1;
};

class Derived : public Base1
{
public:
    virtual int virt1()
    {
        return 150;
    }
    int derivedData;
};

int Global1( Base1* b1)
{
    return b1->virt1();
}

////////////////////////////////////////////////////////////////////////

class Base2
{
public:
    virtual int virt2(){return 200;}
    int data2;
};


class MultipleDerived : public Base1, public Base2
{
public:
    virtual int virt1(){return 150;}
    virtual int virt2(){return 250;}
    int derivedData;
};

int Global2(Base2* b2)
{
    return b2->virt2();
}



int main()
{
    Derived* d = new Derived;
    printf( "%d %d\n", d->virt1(), Global1( d ));
////////////////////////////////////////////////////////////////////////
    MultipleDerived * md = new MultipleDerived;
    printf( "%d %d %d %d\n", 
           md->virt1(), Global1( md ), md->virt2(), Global2( md ));
    
}

//Vtable is created by compiler for each class. 
//When a object is created, there will be a vptr added 
//to the object as a hidden field that points to the address of the v table 
//of the class that object belongs to. 



/**
 * Here is how the compiler works 
 * In the vtable of Base1:
 * +0: Base1::virt1()
 *
 * In the vtable of Derived:
 * +0: Derived::virt1()  //Because virt1() is overriden in Derived
 *
 * For object d:
 * This is the memory layout :
 * d:
 * +0: pointer to vtable of Derived
 * +4: value of data1
 * +8: value of derivedData
 *
 *
 *
 * In the vtable of Base2:
 * +0: Base2::virt2()
 *
 * For object md:
 * This is the memory layout:
 * +0: pointer to vtable of MultipleDerived (For Base 1)
 * +4: value of data1;
 * +8: pointer to vtable of MultipleDerived (For Base 2)
 * +12: value of data2;
 * +16: int derivedData;
 *
 *
 * In the vtable of MultipleDerived (For Base1):
 * +0: MultipleDerived::virt1()  //Because virt1() is overriden in MultipleDerived
 *
 * In the vtable of MultipleDerived (For Base2):
 * +0: MultipleDerived::virt2()  //Because virt2() is overriden in MultipleDerived
 **/














