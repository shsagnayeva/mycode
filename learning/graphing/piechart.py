#!/usr/bin/python3

import matplotlib.pyplot as plt

def main():
    
    labels = 'Butter', 'Cheries', 'Sugar', 'Vanila extract', 'Milk', 'Flour' 
    sizes = [10, 55, 10, 10, 5, 10]
    explode = (0, 0.1, 0, 0, 0, 0) 

    fig1, ax1 = plt.subplots()

    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
    ax1.axis('equal') 

    plt.title("Cherry pie")
    plt.savefig("/home/student/static/pie.png")

if __name__ == "__main__":
    main()
