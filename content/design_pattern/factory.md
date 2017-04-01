Title: Factory Patterns
Date: 2016-04-16
Modified: 2016-04-16 
Category: design pattern
Tags: c++, design pattern

## Simple Factory
*When:* There are many products (ProductA, ProductB, ...) which are derived classes of Product.
Client doesn't care about concrete products. 


```c++
#include "product.h"

class SimpleFactory {
  public:
    // suppose that this implementation is complex and subject to change
    Product* createProduct(std::string type) {
      Product* product;
      if(type.compare("A") == 0) {
        product = new ProductA();
      }
      else if(type.compare("B") == 0) {
        product = new ProductB();
      }
      else if(type.compare("C") == 0) {
        product = new ProductC();
      }

      return product;
    }
};

class Client {
  private:
    SimpleFactory* factory; 

  public:
    Client(SimpleFactory* factory)
      : factory (factory)
    {}

    // doesn't depend on concrete products and their creation
    Product* createProduct(std::string type)
    {
      Product* product = factory->createProduct(type);

      product->doSomethingCommonForProducts();
      
      return product;
    }
};

int main() {
  SimpleFactory* factory = new SimpleFactory();
  Client client = new Client(factory); 

  #with SimpleFactory, product is created with 'type'
  Product* product;
  product = client->createProduct("A"); // create A-type product
  product = client->createProduct("B"); // create B-type product

  #without SimpleFactory
  product = new ProductA();
  product->doSomethingCommonForProducts();
  product = new ProductB();
  product->doSomethingCommonForProducts();
}

```

## Factory Method
*When:* There are many products and they are categorized.

```c++
#depends on Product (abstract), but not concrete products
#doesn't depends on concrete Factories.
class BaseFactory {
  public:
    virtual Product* createProduct(std::string type) = 0;

    void doSomethingCommon(std::string type) {
      Product* product = createProduct(type);
      # ... Something Commone ...
    }
};

# depends on concrete products
# depends on BaseFactory
class FactoryCat0 : public BaseFactory {
  public:
    Product* createProduct(std::string type)
    {
      Product* product;
      if(type.compare("A") == 0) {
        product = new ProductCat0_A();
      }
      else if(type.compare("B") == 0) {
        product = new ProductCat0_B();
      }
      else if(type.compare("C") == 0) {
        product = new ProductCat0_C();
      }

      return product;
    }
};

class FactoryCat1 : public BaseFactory {
    Product* createProduct(std::string type)
    {
      #... create category 1 products ...
    }
};

int main () {
  BaseFactory* factory0 = new FactoryCat0();
  BaseFactory* factory1 = new FactoryCat0();
  Product* product = factory0->createProduct("A"); // Category 0 ProductA
  product = factory1->createProduct("A"); // Category 1 Product A

  return 0;
}
```

## Abstract Factory
*when:* create a family of related products




