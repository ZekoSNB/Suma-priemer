import argparse

parser = argparse.ArgumentParser(description='how much numberas you need')
parser.add_argument('again', type=int, help='How much numbers you need to input')
args = parser.parse_args()


def main(number):
    numslist = []
    total = 0
    for i in range(number):
        maininput = float(input(f'Zadaj cislo {i+1} '))
        numslist.append(maininput)

    for j in range(len(numslist)):
        total = total+numslist[j]

    priemer = total / len(numslist)
    print(f'Suma: {total} || Priemer: {priemer}')

if __name__ == '__main__':
    main(args.again)
