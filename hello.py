"""
pokud toto spoustim (main) tak se mi spusti jen import module, coz znamena nic z modulu co je v main
"""

def main():
    print("hello world")
    import module
    module.hello("Second hello")

""" 
mohu mit __main__ az na konci souboru a muzu na funkci __main__ pouzivat anotace (@dataclass)
"""
if __name__== "__main__":
    main()
