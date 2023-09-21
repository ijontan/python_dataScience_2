from load_csv import load
import matplotlib.pyplot as plt


def getvalue(string: str) -> int:
    """get value from string"""
    value = 1
    if string[-1] == "B":
        value = 1000000000
    elif string[-1] == "M":
        value = 1000000
    elif string[-1] == "k":
        value = 1000
    else:
        return float(string)
    return float(string[:-1]) * value


def main():
    """main function"""
    try:
        a = "income_per_person_gdppercapita_ppp_inflation_adjusted.csv"
        b = "life_expectancy_years.csv"
        year = "1900"
        income_data = load(a)
        if income_data is None:
            return
        life_data = load(b)
        if life_data is None:
            return

        plt.scatter(income_data[year], life_data[year], color="blue")
        plt.xlabel("Gross Domestic Product")
        plt.ylabel("Life Expectancy")
        plt.xscale("log")
        plt.title(year)
        plt.show()
    except Exception as e:
        print(e)
    except KeyboardInterrupt:
        print("\b\bInterrupted by user.")


if __name__ == "__main__":
    main()
