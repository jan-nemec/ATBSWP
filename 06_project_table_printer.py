# table_printer.py

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]


def printTable(itemsList):
    """Takes a list of lists and display it in a well-organized table
    with each column right justified."""
    colWidths = [0] * len(itemsList)

    for i in range(len(itemsList)):
        colWidths[i] = max(len(item) for item in itemsList[i])
        # colWidths = max(dataLists[i], key=len)  # cherries
        # for j in range(len(itemsList[i])):
        #    if colWidths[i] < len(itemsList[i][j]):
        #        colWidths[i] = len(itemsList[i][j])

    # print(colWidths)

    for k in range(len(itemsList[0])):
        for l in range(len(itemsList)):
            print(itemsList[l][k].rjust(colWidths[l] + 1), end='')
        print()


printTable(tableData)
