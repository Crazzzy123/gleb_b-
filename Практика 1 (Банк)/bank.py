import account
import cash1

def main():
    rate = int(input('Vvedite stavky:'))
    money = int(input('Vvedite summy:'))
    period = int(input('Vvedite period:'))
    result = account.calculate_income(rate,period,money)

    result2 = cash1.perevod(result)
    print ("Parametri scheta:\n", "Summ",money, "\n", "Stavki", rate, "\n", "Period", period, "\n", "Obsh sum", result, "\n")
if __name__=="__main__":
    main()
