from load_csv import load
import matplotlib.pyplot as plt
import numpy as np


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
        data = load("population_total.csv")
        if data is None:
            return
        country1 = "China"
        country2 = "India"
        years = np.array(data.columns[1:]).astype(int)
        country1_data = data[data["country"] == country1].values[0, 1:]
        country1_data = [getvalue(i) for i in country1_data]
        country2_data = data[data["country"] == country2].values[0, 1:]
        country2_data = [getvalue(i) for i in country2_data]

        plt.plot(years, country1_data, color="green", label=country1)
        plt.plot(years, country2_data, color="blue", label=country2)
        plt.xlabel("Year")
        plt.ylabel("Population")
        plt.title("Population Projects")
        plt.xticks(range(1800, 2081, 40))
        plt.legend()
        plt.show()
    except Exception as e:
        print(e)
    except KeyboardInterrupt:
        print("\b\bInterrupted by user.")


if __name__ == "__main__":
    main()
