#this is called maintainability
import calculator
if __name__=='__main__':
    print("testing calc module")
    result =calculator.sum(10,20)
    print(result)
    if True:
        import os  #lazy loading , only load when condition is satisfies