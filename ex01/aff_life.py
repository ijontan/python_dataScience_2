from load_csv import load
import matplotlib.pyplot as plt
import numpy as np


def main():
    """main function"""
    try:
        data = load("life_expectancy_years.csv")
        if data is None:
            return
        country = "Malaysia"
        years = np.array(data.columns[1:]).astype(int)
        one_country = data[data["country"] == country].values[0, 1:]
        one_country = one_country.astype(float)

        plt.plot(years, one_country)
        plt.xlabel("Year")
        plt.ylabel("Life expectancy")
        plt.title(f"Life expectancy in {country}")
        plt.xticks(range(1800, 2081, 40))
        plt.show()
    except Exception as e:
        print(e)
    except KeyboardInterrupt:
        print("\b\bInterrupted by user.")


if __name__ == "__main__":
    main()
