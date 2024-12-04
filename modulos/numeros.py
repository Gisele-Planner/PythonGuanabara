def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError,TypeError):
            print(f'\33[0;31mERRO! Por valor Digite um número inteiro válido.\33[m')
            continue
        except (KeyboardInterrupt):
            print(f'\33[0;31mUsuário preferiu não digitar esse número.\33[m')
        except Exception as erro:
            print(f'\33[0;31mERRO! Na classe {erro.__cause__}.\33[m')
        else:
            return n
    

def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError,TypeError):
            print(f'\33[0;31mERRO! Por valor Digite um número real válido.\33[m')
            continue
        except (KeyboardInterrupt):
            print(f'\33[0;31mUsuário preferiu não digitar esse número.\33[m')
        except Exception as erro:
            print(f'\33[0;31mERRO! Na classe {erro.__cause__}.\33[m')
        else:
            return n
        